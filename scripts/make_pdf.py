"""Build the site and print the whole manual to one PDF with headless Chrome.

    uv run python scripts/make_pdf.py            # -> dist/rotse-observer-manual-<date>.pdf
    uv run python scripts/make_pdf.py --no-build # reuse the existing site/

Needs Google Chrome or Chromium. Set CHROME=/path/to/chrome if it isn't found.
"""

from __future__ import annotations

import argparse
import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DIST = ROOT / "dist"

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


def find_chrome() -> str:
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for c in CHROME_CANDIDATES:
        path = c if os.path.isabs(c) else shutil.which(c)
        if path and os.path.exists(path):
            return path
    sys.exit("Chrome/Chromium not found. Install it or set CHROME=/path/to/chrome.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-build", action="store_true", help="don't run mkdocs build first")
    ap.add_argument("-o", "--output", type=Path, help="output PDF path")
    args = ap.parse_args()

    if not args.no_build:
        subprocess.run(["mkdocs", "build", "--strict"], cwd=ROOT, check=True)

    page = SITE / "print_page" / "index.html"
    if not page.exists():
        sys.exit(f"{page} not found: build the site first.")

    out = args.output or DIST / f"rotse-observer-manual-{datetime.date.today()}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    # #pdf tells javascripts/print.js to switch to print mode (light colours,
    # open boxes, all tabs). The time budget lets Mermaid and MathJax finish.
    cmd = [
        find_chrome(),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=15000",
        f"--print-to-pdf={out}",
        page.as_uri() + "#pdf",
    ]
    subprocess.run(cmd, check=True, timeout=180, capture_output=True)
    print(f"PDF written: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


if __name__ == "__main__":
    main()
