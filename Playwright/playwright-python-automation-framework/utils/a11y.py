from typing import List, Dict
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import AxePlaywright


def run_accessibility_check(page: Page) -> List[Dict]:
    """Run axe-core accessibility checks and return list of violations."""
    axe = AxePlaywright(page)
    results = axe.run()
    return results.get("violations", [])
