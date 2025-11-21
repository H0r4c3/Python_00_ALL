from playwright.sync_api import expect
from .base_page import BasePage


class LoginPage(BasePage):
    """Login page and related flows."""

    def open(self, base_url: str) -> None:
        self.page.goto(base_url)
        self.page.get_by_role("link", name="My account").click()

    def login(self, email: str, password: str) -> None:
        self.page.get_by_label("Email").fill(email)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def assert_logged_in(self) -> None:
        expect(self.page.get_by_text("Logout")).to_be_visible()

    def assert_login_error(self) -> None:
        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()
