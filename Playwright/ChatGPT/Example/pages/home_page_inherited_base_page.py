from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page Object for the Practice Software Testing homepage."""

    def __init__(self, page):
        super().__init__(page)
        self.url = "https://practicesoftwaretesting.com/"
        self.logo = page.locator("header img[alt='Practice Software Testing']")

    def open(self):
        self.goto(self.url)
        self.wait_for_load()
        expect(self.logo).to_be_visible()
