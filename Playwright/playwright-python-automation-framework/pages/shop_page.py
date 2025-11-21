from playwright.sync_api import expect
from .base_page import BasePage


class ShopPage(BasePage):
    """Shop/catalog page."""

    def open(self, base_url: str) -> None:
        self.page.goto(f"{base_url}/shop")

    def select_product(self, name: str) -> None:
        self.page.get_by_text(name, exact=True).click()

    def add_to_cart(self) -> None:
        self.page.get_by_role("button", name="Add to cart").click()

    def assert_cart_visible(self) -> None:
        expect(self.page.get_by_text("Cart")).to_be_visible()
