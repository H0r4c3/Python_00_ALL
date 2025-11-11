# test_navigation.py
"""Navigation and wait tests"""
from playwright.sync_api import Page, expect
import time


class TestNavigation:
    """Test navigation and waiting"""
    
    def test_go_back(self, page: Page) -> None:
        """Test: Go back (Example 24)"""
        page.goto("https://www.google.com")
        page.goto("https://www.wikipedia.org")
        page.go_back()
        expect(page).to_have_url("https://www.google.com/")
    
    def test_go_forward(self, page: Page) -> None:
        """Test: Go forward (Example 25)"""
        page.goto("https://www.google.com")
        page.goto("https://www.wikipedia.org")
        page.go_back()
        page.go_forward()
        expect(page).to_have_url('wikipedia')
    
    def test_reload_page(self, page: Page) -> None:
        """Test: Reload page (Example 26)"""
        page.goto("https://www.google.com")
        page.reload()
        expect(page).to_have_title('Google')
    
    def test_wait_for_selector(self, page: Page) -> None:
        """Test: Wait for selector (Example 59)"""
        page.goto("https://www.google.com")
        page.fill("textarea[name='q']", "Playwright")
        page.press("textarea[name='q']", "Enter")
        page.wait_for_selector("h3", timeout=10000)
        assert page.locator("h3").count() > 0
    
    def test_wait_for_timeout(self, page: Page) -> None:
        """Test: Wait for timeout (Example 30)"""
        page.goto("https://www.google.com")
        start = time.time()
        page.wait_for_timeout(2000)
        elapsed = time.time() - start
        assert elapsed >= 2