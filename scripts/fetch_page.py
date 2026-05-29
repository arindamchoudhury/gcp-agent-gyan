"""
fetch_page.py — fetch a JavaScript-rendered page and save its text content to cache.

Usage:
    python fetch_page.py <url> [--slug <slug>] [--out <cache-dir>] [--timeout <ms>]

Outputs:
    Saves extracted text to <cache-dir>/<slug>.txt (default cache dir: ../cache/web)
    Prints the saved file path to stdout on success.

Requirements:
    pip install playwright
    Uses the system Chrome installation — no separate browser download needed.
"""

import argparse
import re
import sys
from pathlib import Path

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DEFAULT_CACHE_DIR = Path(__file__).parent.parent / "cache" / "web"

# JS that returns innerText of the container holding the next-slide button.
# Used once per card to capture the currently visible slide.
_CAROUSEL_SLIDE_TEXT_JS = """
() => {
    const btn = document.querySelector('[aria-label="Go to next slide"]');
    if (!btn) return '';
    let el = btn.parentElement;
    for (let i = 0; i < 10; i++) {
        if (!el || el === document.body) return '';
        if (el.offsetHeight > 100 && el.offsetWidth > 200) break;
        el = el.parentElement;
    }
    return el ? el.innerText.trim() : '';
}
"""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def slug_from_url(url: str) -> str:
    url = re.sub(r"https?://", "", url)
    url = re.sub(r"[#?].*$", "", url)
    url = re.sub(r"[^\w]+", "-", url)
    return url[:80].strip("-")


def expand_all_interactive(page) -> None:
    """Click every interactive element that might reveal hidden content."""

    # 1. Transcript toggle buttons
    for label in ["Transcript", "Show transcript", "View transcript"]:
        try:
            btn = page.get_by_text(label, exact=True).first
            if btn and btn.is_visible():
                btn.click()
                page.wait_for_timeout(1500)
                print(f"Clicked '{label}' button", file=sys.stderr)
                break
        except Exception:
            pass

    # 2. Click all collapsed accordions / expandable items.
    #    IMPORTANT: only target trigger elements (buttons, headers), NOT body/container
    #    divs that also happen to contain "accordion" in their class. Clicking body
    #    divs after opening a header can re-close the accordion.
    expand_selectors = [
        "button[aria-expanded='false']",
        "[role='button'][aria-expanded='false']",
        "summary",                                    # <details>/<summary> elements
        "button[class*='accordion__header']",
        "button[class*='accordion-header']",
        "[class*='accordion__header']:not([aria-expanded='true'])",
        "[class*='accordion-header']:not([aria-expanded='true'])",
        "[class*='card__header']",
        "[class*='card-header']",
        "[class*='item__header']",
        "[class*='item-header']",
        "[class*='panel-heading']",
    ]
    for selector in expand_selectors:
        try:
            elements = page.query_selector_all(selector)
            for el in elements:
                try:
                    if el.is_visible():
                        el.click()
                        page.wait_for_timeout(400)
                except Exception:
                    pass
            if elements:
                print(f"Clicked {len(elements)} '{selector}' element(s)", file=sys.stderr)
        except Exception:
            pass

    # 3. Click all tab buttons / nav tabs to reveal tab content
    tab_selectors = [
        "[role='tab']",
        ".blocks-tabs__header-item",
        "[class*='tab__button']",
        "[class*='tab-button']",
        "[class*='tab__item']",
        "[class*='tab-item']",
        "[class*='nav-link']",
    ]
    for selector in tab_selectors:
        try:
            tabs = page.query_selector_all(selector)
            for tab in tabs:
                try:
                    if tab.is_visible():
                        tab.click()
                        page.wait_for_timeout(600)
                except Exception:
                    pass
            if tabs:
                print(f"Clicked {len(tabs)} tab(s) via '{selector}'", file=sys.stderr)
        except Exception:
            pass

    # 4. Reveal buttons
    for label in ["Show more", "Read more", "Learn more", "View details", "Reveal", "See more"]:
        try:
            btn = page.get_by_text(label, exact=False).first
            if btn and btn.is_visible():
                btn.click()
                page.wait_for_timeout(800)
                print(f"Clicked reveal button: '{label}'", file=sys.stderr)
        except Exception:
            pass

    page.wait_for_timeout(1000)


def extract_tab_panels(page) -> str:
    """Extract text from all tab panels, including CSS-hidden ones.

    Tab widgets (exclusive: only one panel visible at a time) leave all but
    the last-clicked panel hidden when the page is extracted via inner_text().
    This function temporarily un-hides each panel to read its text, then
    restores the original visibility.
    """
    try:
        panels = page.evaluate("""
        () => {
            const selectors = [
                '[role="tabpanel"]',
                '.blocks-tabs__content-item',
                '[class*="tab__panel"]',
                '[class*="tab-panel"]',
                '[class*="tabpanel"]',
            ];
            for (const sel of selectors) {
                const els = Array.from(document.querySelectorAll(sel));
                if (els.length < 2) continue;
                const results = [];
                for (const el of els) {
                    const prev = el.style.display;
                    el.style.display = 'block';
                    const text = el.innerText.trim();
                    el.style.display = prev;
                    if (text.length > 30) results.push(text);
                }
                if (results.length >= 2) return results;
            }
            return [];
        }
        """)
    except Exception:
        return ""

    if not panels:
        return ""

    print(f"Tab panels: captured {len(panels)} panel(s)", file=sys.stderr)
    return "\n\n=== Tab Panels ===\n\n" + "\n\n---\n\n".join(panels)


def extract_carousel_cards(page) -> str:
    """Walk through flashcard carousels (next-slide button pattern) and collect all cards.

    Google Cloud training uses a carousel where each card has a front (question)
    and a flippable back (answer). Cards 2-N are hidden by CSS until navigated to.
    This function navigates through every card, flips each one, and returns all text.
    """
    # Only run if a carousel navigation button exists
    if not page.query_selector("[aria-label='Go to next slide']"):
        return ""

    cards = []
    seen = set()

    for _ in range(30):  # safety cap
        # Capture the currently visible card (front side)
        text = page.evaluate(_CAROUSEL_SLIDE_TEXT_JS)
        key = text[:80]
        if key in seen:
            break  # wrapped back to start
        seen.add(key)

        # Flip to the back side — click all visible flip buttons in the slide
        try:
            for btn in page.query_selector_all(".flashcard-side-flip__btn"):
                if btn.is_visible():
                    btn.click()
                    page.wait_for_timeout(400)
                    break  # one click flips the card; stop after first visible hit
        except Exception:
            pass

        # Capture the back side
        text_back = page.evaluate(_CAROUSEL_SLIDE_TEXT_JS)
        if text_back[:80] not in seen:
            seen.add(text_back[:80])
            cards.append(text_back)
        else:
            cards.append(text)  # back was same as front (no flip); keep front

        # Navigate to the next card
        try:
            btn = page.query_selector("[aria-label='Go to next slide']")
            if btn and btn.is_visible():
                btn.click()
                page.wait_for_timeout(700)
            else:
                break
        except Exception:
            break

    if not cards:
        return ""

    print(f"Carousel: captured {len(cards)} card(s)", file=sys.stderr)
    separator = "\n\n--- next card ---\n\n"
    return "\n\n=== Knowledge Check Cards ===\n\n" + separator.join(cards)


def extract_images(page, base_url: str) -> str:
    """Collect URLs of meaningful content images (diagrams, screenshots).

    Skips tiny images (icons, bullets) and data-URI blobs.
    Returns a formatted block to append to the cache file, or '' if none found.
    """
    try:
        imgs = page.evaluate(
            """(baseUrl) => {
                const results = [];
                const seen = new Set();
                for (const img of document.querySelectorAll('img')) {
                    const src = img.currentSrc || img.src || '';
                    if (!src || src.startsWith('data:') || seen.has(src)) continue;
                    // Skip tiny images (icons/bullets/UI chrome)
                    const w = img.naturalWidth || img.width || 0;
                    const h = img.naturalHeight || img.height || 0;
                    if (w < 200 || h < 100) continue;
                    seen.add(src);
                    results.push({src, alt: img.alt || '', w, h});
                }
                return results;
            }""",
            base_url,
        )
    except Exception:
        return ""

    if not imgs:
        return ""

    lines = ["\n\n=== Images ===\n"]
    for img in imgs:
        alt = img["alt"] or "diagram"
        lines.append(f"![]({img['src']})")
        lines.append(f"*{alt} ({img['w']}×{img['h']})*\n")
    print(f"Images: captured {len(imgs)} image(s)", file=sys.stderr)
    return "\n".join(lines)


def fetch(url: str, slug: str, out_dir: Path, timeout_ms: int) -> Path:
    from playwright.sync_api import sync_playwright

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{slug}.txt"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        page = browser.new_page()

        print(f"Fetching: {url}", file=sys.stderr)
        page.goto(url, wait_until="networkidle", timeout=timeout_ms)

        try:
            page.wait_for_function(
                """() => {
                    const body = document.body.innerText.toLowerCase();
                    return body.length > 200 && !body.includes('your content is loading');
                }""",
                timeout=timeout_ms,
            )
        except Exception as e:
            print(f"Wait timed out or failed: {e}", file=sys.stderr)

        page.wait_for_timeout(1000)

        # Expand accordions, tabs, transcripts, etc.
        expand_all_interactive(page)

        # Collect carousel/flashcard content (hidden-by-CSS slides)
        carousel_text = extract_carousel_cards(page)

        # Collect all tab panel content (hidden panels excluded from inner_text)
        tab_panel_text = extract_tab_panels(page)

        # Collect content image URLs (diagrams, screenshots)
        image_block = extract_images(page, url)

        # Final re-open pass: any accordion that got accidentally re-closed
        # (e.g. by a tab switch or a body-div click) is reopened here.
        try:
            still_closed = page.query_selector_all(
                "button[aria-expanded='false'], [class*='accordion__header'][aria-expanded='false']"
            )
            for el in still_closed:
                if el.is_visible():
                    el.click()
                    page.wait_for_timeout(300)
            if still_closed:
                print(f"Re-open pass: clicked {len(still_closed)} still-closed element(s)", file=sys.stderr)
        except Exception:
            pass
        page.wait_for_timeout(500)

        # Extract main visible content
        content = ""
        for selector in ["main", "article", "[role='main']", "#content", ".content", ".lesson", ".slide", "body"]:
            try:
                el = page.query_selector(selector)
                if el:
                    text = el.inner_text()
                    if len(text.strip()) > 200:
                        content = text
                        print(f"Extracted from: {selector}", file=sys.stderr)
                        break
            except Exception:
                continue

        browser.close()

    if carousel_text:
        content = content + "\n\n" + carousel_text
    if tab_panel_text:
        content = content + "\n\n" + tab_panel_text
    if image_block:
        content = content + image_block

    if not content.strip():
        print("WARNING: extracted content is empty.", file=sys.stderr)
        sys.exit(1)

    out_file.write_text(content, encoding="utf-8")
    print(f"Saved {len(content)} chars to: {out_file}", file=sys.stderr)
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Fetch a JS-rendered page to text cache.")
    parser.add_argument("url", help="URL to fetch")
    parser.add_argument("--slug", help="Cache file slug (auto-derived from URL if omitted)")
    parser.add_argument("--out", help="Output cache directory", default=str(DEFAULT_CACHE_DIR))
    parser.add_argument("--timeout", type=int, default=30000, help="Page load timeout in ms (default: 30000)")
    args = parser.parse_args()

    slug = args.slug or slug_from_url(args.url)
    out_dir = Path(args.out)
    out_file = fetch(args.url, slug, out_dir, args.timeout)
    print(str(out_file))


if __name__ == "__main__":
    main()
