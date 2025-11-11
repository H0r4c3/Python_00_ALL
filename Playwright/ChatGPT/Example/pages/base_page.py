from playwright.sync_api import Page, expect
import os
from datetime import datetime

class BasePage:
    """Base class for all page objects — holds common actions."""

    def __init__(self, page: Page):
        self.page = page

    # ---------- Navigation ----------
    def goto(self, url: str):
        """Navigate to a given URL."""
        self.page.goto(url)

    def wait_for_load(self, state: str = "networkidle"):
        """Wait until page finishes loading (DOM + network idle)."""
        self.page.wait_for_load_state(state)

    # ---------- Information ----------
    def get_title(self) -> str:
        """Return the current page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Return the current URL."""
        return self.page.url

    # ---------- Utilities ----------
    def take_screenshot(self, name: str = "screenshot"):
        """Take screenshot and save with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join("test-results", f"{name}_{timestamp}.png")
        os.makedirs("test-results", exist_ok=True)
        self.page.screenshot(path=path)
        print(f"📸 Screenshot saved: {path}")

    def wait_and_click(self, selector: str):
        """Wait until element is visible and then click it."""
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def fill_field(self, selector: str, value: str):
        """Wait and fill input field."""
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)
