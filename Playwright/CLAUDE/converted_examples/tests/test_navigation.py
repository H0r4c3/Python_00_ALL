"""Navigation tests using Page Object Model"""
from playwright.sync_api import Page, expect
from pages.google_page import GooglePage
from pages.wikipedia_page import WikipediaPage
import time


class TestNavigationWithPOM:
    """Navigation tests with Page Objects"""
    
    def test_go_back(self, page: Page) -> None:
        """Test: Go back using page objects"""
        google_page = GooglePage(page)
        wikipedia_page = WikipediaPage(page)
        
        # Visit Google
        google_page.navigate()
        expect(page).to_have_url("https://www.google.com/")
        
        # Visit Wikipedia
        wikipedia_page.navigate()
        assert wikipedia_page.is_on_wikipedia()
        
        # Go back to Google
        page.go_back()
        expect(page).to_have_url("https://www.google.com/")
    
    def test_go_forward(self, page: Page) -> None:
        """Test: Go forward using page objects"""
        google_page = GooglePage(page)
        wikipedia_page = WikipediaPage(page)
        
        # Visit both pages
        google_page.navigate()
        wikipedia_page.navigate()
        
        # Go back
        page.go_back()
        expect(page).to_have_url("https://www.google.com/")
        
        # Go forward
        page.go_forward()
        assert wikipedia_page.is_on_wikipedia()
    
    def test_reload_page(self, page: Page) -> None:
        """Test: Reload page using page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        
        # Get initial title
        initial_title = google_page.get_title()
        
        # Reload
        page.reload()
        
        # Title should still be the same
        assert google_page.get_title() == initial_title
    
    def test_wait_for_selector(self, page: Page) -> None:
        """Test: Wait for selector after navigation"""
        google_page = GooglePage(page)
        google_page.navigate()
        google_page.search("Playwright")
        
        # Wait for results
        page.wait_for_selector("h3", timeout=10000)
        assert google_page.get_results_count() > 0
    
    def test_wait_for_timeout(self, page: Page) -> None:
        """Test: Wait for timeout"""
        google_page = GooglePage(page)
        google_page.navigate()
        
        start = time.time()
        page.wait_for_timeout(2000)
        elapsed = time.time() - start
        
        assert elapsed >= 2
    
    def test_scroll_to_element(self, page: Page) -> None:
        """Test: Scroll element into view"""
        wikipedia_page = WikipediaPage(page)
        wikipedia_page.navigate()
        
        # Scroll to footer
        wikipedia_page.scroll_to_footer()
        
        # Footer should be visible
        assert wikipedia_page.is_footer_visible()