"""Inspect the card deck DOM structure on a Google Cloud training lesson."""
import json
from playwright.sync_api import sync_playwright

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
URL = "https://storage.googleapis.com/cloud-training/cls-html5-courses/C-AGTSPI-B/v1.0.1/index.html#/lessons/CoL6bbMndCKfO9ZhVWtgXpl8MyWpYUXM"

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME, headless=True, args=["--no-sandbox"])
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle", timeout=45000)
    # Wait until loading placeholder disappears
    page.wait_for_function(
        """() => {
            const t = document.body.innerText.toLowerCase();
            return t.length > 500 && !t.includes('your content is loading');
        }""",
        timeout=45000,
    )
    page.wait_for_timeout(2000)
    # Scroll down to trigger lazy-rendered sections, then back up
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1500)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)

    # Find "Information retrieval" text and inspect its surrounding DOM
    info = page.evaluate("""
    () => {
        // Find text nodes containing the accordion headers
        const targets = ['Information retrieval', 'Task automation', 'Communication', 'Data analysis'];
        const results = [];
        for (const target of targets) {
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            while (walker.nextNode()) {
                if (walker.currentNode.textContent.includes(target)) {
                    const el = walker.currentNode.parentElement;
                    // Walk up to find the clickable ancestor
                    let clickable = el;
                    for (let i = 0; i < 6; i++) {
                        if (!clickable) break;
                        const tag = clickable.tagName;
                        const role = clickable.getAttribute('role');
                        const ariaExp = clickable.getAttribute('aria-expanded');
                        if (tag === 'BUTTON' || role === 'button' || ariaExp !== null) {
                            results.push({
                                target,
                                tag,
                                role,
                                ariaExpanded: ariaExp,
                                class: clickable.className.substring(0, 100),
                                visible: clickable.offsetWidth > 0,
                            });
                            break;
                        }
                        clickable = clickable.parentElement;
                    }
                    // Also capture the immediate parent chain
                    if (results.length === 0 || results[results.length-1].target !== target) {
                        let chain = [];
                        let cur = el;
                        for (let i = 0; i < 5; i++) {
                            if (!cur || cur === document.body) break;
                            chain.push({tag: cur.tagName, class: cur.className.substring(0,60), ariaExp: cur.getAttribute('aria-expanded')});
                            cur = cur.parentElement;
                        }
                        results.push({target, notFound: true, chain});
                    }
                    break;
                }
            }
        }
        return results;
    }
    """)
    print("Accordion structure:")
    for item in info:
        print(" ", json.dumps(item))
    browser.close()
