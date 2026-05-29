"""
extract_pdf.py — extract text from a PDF and save to cache.

Usage:
    python extract_pdf.py <pdf_path> [--slug <slug>] [--out <cache-dir>]

Outputs:
    Saves extracted text to <cache-dir>/<slug>.txt
    Prints the saved file path to stdout on success.
"""

import argparse
import re
import sys
from pathlib import Path

DEFAULT_CACHE_DIR = Path(__file__).parent.parent / "cache" / "pdf"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def extract(pdf_path: Path, slug: str, out_dir: Path) -> Path:
    import pymupdf

    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{slug}.txt"

    doc = pymupdf.open(str(pdf_path))
    pages = []
    for page in doc:
        text = page.get_text("text")
        if text.strip():
            pages.append(text)
    doc.close()

    content = "\n\n".join(pages)
    if not content.strip():
        print("WARNING: extracted content is empty.", file=sys.stderr)
        sys.exit(1)

    out_file.write_text(content, encoding="utf-8")
    print(f"Saved {len(content)} chars ({len(pages)} pages) to: {out_file}", file=sys.stderr)
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Extract PDF text to cache.")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--slug", help="Cache file slug (auto-derived from filename if omitted)")
    parser.add_argument("--out", help="Output cache directory", default=str(DEFAULT_CACHE_DIR))
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    slug = args.slug or slugify(pdf_path.stem)
    out_dir = Path(args.out)
    out_file = extract(pdf_path, slug, out_dir)
    print(str(out_file))


if __name__ == "__main__":
    main()
