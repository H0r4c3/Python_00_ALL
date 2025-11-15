from playwright.sync_api import Page, expect

class HomePage:
    """Page Object for the Practice Software Testing homepage."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practicesoftwaretesting.com/"
        # Example locators
        self.logo = page.locator("header img[alt='Practice Software Testing']")
        self.search_box = page.locator("input[name='q']")
        self.cart_icon = page.locator("#cart-icon")

    def open(self):
        """Navigate to the homepage."""
        self.page.goto(self.url)

    def get_title(self) -> str:
        """Return current page title."""
        return self.page.title()

    def search(self, text: str):
        """Perform a search."""
        self.search_box.fill(text)
        self.search_box.press("Enter")

    def assert_home_loaded(self):
        """Verify the homepage loaded correctly."""
        expect(self.logo).to_be_visible()
        expect(self.page).to_have_url(self.url)
