"""Navigation tests using Page Object Model"""
from playwright.sync_api import Page, expect
#from pages.practicesoftwaretesting_page import PracticeStorePage
from pages.practice_store_page import PracticeStorePage
from pages.wikipedia_page import WikipediaPage
import time


class TestNavigationWithPOM:
    """Navigation tests with Page Objects"""
    
    def test_go_back(self, page: Page) -> None:
        """Test: Go back using page objects"""
        practicesoftwaretesting_page = PracticeStorePage(page)
        wikipedia_page = WikipediaPage(page)
        
        # Visit Google
        practicesoftwaretesting_page.navigate()
        expect(page).to_have_url("https://practicesoftwaretesting.com/")
        
        # Visit Wikipedia
        wikipedia_page.navigate()
        assert wikipedia_page.is_on_wikipedia()
        
        # Go back to Google
        page.go_back()
        expect(page).to_have_url("https://practicesoftwaretesting.com/")
    
    def test_go_forward(self, page: Page) -> None:
        """Test: Go forward using page objects"""
        practicesoftwaretesting_page = PracticeStorePage(page)
        wikipedia_page = WikipediaPage(page)
        
        # Visit both pages
        practicesoftwaretesting_page.navigate()
        wikipedia_page.navigate()
        
        # Go back
        page.go_back()
        expect(page).to_have_url("https://practicesoftwaretesting.com/")
        
        # Go forward
        page.go_forward()
        assert wikipedia_page.is_on_wikipedia()
    
    def test_reload_page(self, page: Page) -> None:
        """Test: Reload page using page object"""
        practicesoftwaretesting_page = PracticeStorePage(page)
        practicesoftwaretesting_page.navigate()
        
        # Get initial title
        initial_title = practicesoftwaretesting_page.get_title()
        
        # Reload
        page.reload()
        
        # Title should still be the same
        assert practicesoftwaretesting_page.get_title() == initial_title
    
    def test_wait_for_selector(self, page: Page) -> None:
        """Test: Wait for selector after navigation"""
        practicesoftwaretesting_page = PracticeStorePage(page)
        practicesoftwaretesting_page.navigate()
        practicesoftwaretesting_page.search("hammer")
        
        # Wait for results
        page.wait_for_selector("h3", timeout=10000)
        assert practicesoftwaretesting_page.get_product_count() > 0
    
    def test_wait_for_timeout(self, page: Page) -> None:
        """Test: Wait for timeout"""
        practicesoftwaretesting_page = PracticeStorePage(page)
        practicesoftwaretesting_page.navigate()
        
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