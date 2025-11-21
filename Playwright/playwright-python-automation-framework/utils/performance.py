from playwright.sync_api import Page


def get_load_time(page: Page) -> int:
    """Return page load time in ms using NavigationTiming."""
    timing = page.evaluate("() => performance.timing")
    return timing["loadEventEnd"] - timing["navigationStart"]
