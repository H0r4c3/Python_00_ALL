from playwright.sync_api import Page, expect


class BasePage:
    """Base class with common helpers for all pages."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: str) -> None:
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str) -> None:
        self.page.locator(locator).fill(text)

    def assert_visible(self, locator: str) -> None:
        expect(self.page.locator(locator)).to_be_visible()

    def screenshot(self, path: str) -> None:
        self.page.screenshot(path=path)

    def verify_screenshot(self, name: str) -> None:
        """Playwright will manage baseline snapshot for you."""
        expect(self.page).to_have_screenshot(name)
