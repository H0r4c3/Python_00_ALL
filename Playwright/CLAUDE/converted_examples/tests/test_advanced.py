# test_advanced.py
"""Advanced Playwright features"""
from playwright.sync_api import Page, expect


class TestAdvanced:
    """Advanced tests"""
    
    def test_handle_dialog(self, page: Page) -> None:
        """Test: Handle alert (Example 64)"""
        page.on("dialog", lambda dialog: dialog.accept())
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")
        page.click("button:has-text('Click for JS Alert')")
        # If no error, dialog was handled
        assert True
    
    def test_multiple_pages(self, page: Page) -> None:
        """Test: Handle popup (Example 68)"""
        page.goto("https://the-internet.herokuapp.com/windows")
        
        with page.expect_popup() as popup_info:
            page.click("a:has-text('Click Here')")
        
        new_page = popup_info.value
        expect(new_page).to_have_title('New Window')
        new_page.close()
    
    def test_drag_and_drop(self, page: Page) -> None:
        """Test: Drag and drop (Example 63)"""
        page.goto("https://the-internet.herokuapp.com/drag_and_drop")
        page.drag_and_drop("#column-a", "#column-b")
        # Verify columns swapped
        assert page.locator("#column-a").inner_text() == "B"
    
    def test_mobile_emulation(self, playwright, browser) -> None:
        """Test: Mobile device (Example 56)"""
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        page = context.new_page()
        
        page.goto("https://www.google.com")
        viewport = page.viewport_size
        assert viewport["width"] == 390  # iPhone 12 width
        
        context.close()
    
    def test_evaluate_javascript(self, page: Page) -> None:
        """Test: Run JavaScript (Example 50)"""
        page.goto("https://www.google.com")
        result = page.evaluate("() => document.title")
        assert "Google" in result