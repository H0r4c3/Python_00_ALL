"""Locator tests using Page Object Model"""
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


class TestLocatorsWithPOM:
    """Locator tests with Page Objects"""
    
    def test_login_with_page_object(self, page: Page) -> None:
        """Test: Login using page object"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("tomsmith", "SuperSecretPassword!")
        
        assert login_page.is_logged_in()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    
    def test_login_error_message(self, page: Page) -> None:
        """Test: Invalid login using page object"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("wronguser", "wrongpass")
        
        flash_message = login_page.get_flash_message()
        assert "invalid" in flash_message.lower()
    
    def test_logout_button_after_login(self, page: Page) -> None:
        """Test: Logout button appears after login"""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("tomsmith", "SuperSecretPassword!")
        
        assert login_page.is_logout_button_visible()