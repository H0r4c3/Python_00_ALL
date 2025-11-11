"""Basic Playwright operations using Page Object Model"""
from playwright.sync_api import Page, expect
from pages.google_page import GooglePage
from pages.base_page import BasePage


class TestBasicsWithPOM:
    """Basic operations with Page Object Model"""
    
    def test_navigate_to_page(self, page: Page) -> None:
        """Test: Navigate using page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        expect(page).to_have_title("Google")
    
    def test_get_page_title(self, page: Page) -> None:
        """Test: Get page title via page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        title = google_page.get_title()
        assert "Google" in title
    
    def test_search_functionality(self, page: Page) -> None:
        """Test: Search using page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        google_page.search("Playwright Python")
        
        page.wait_for_load_state("networkidle")
        assert "search" in google_page.get_url()
    
    def test_check_search_box_visible(self, page: Page) -> None:
        """Test: Check element visibility via page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        assert google_page.is_search_box_visible()
    
    def test_take_screenshot(self, page: Page) -> None:
        """Test: Screenshot via page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        google_page.screenshot("screenshots/google_pom.png")