"""The Internet - Login page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page at the-internet.herokuapp.com"""
    
    URL = "https://the-internet.herokuapp.com/login"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")
    
    def navigate(self) -> None:
        """Navigate to login page"""
        self.navigate_to(self.URL)
    
    def login(self, username: str, password: str) -> None:
        """Perform login"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def get_flash_message(self) -> str:
        """Get flash message text"""
        return self.flash_message.inner_text()
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in"""
        return "/secure" in self.get_url()
    
    def is_logout_button_visible(self) -> bool:
        """Check if logout button is visible"""
        return self.logout_button.is_visible()