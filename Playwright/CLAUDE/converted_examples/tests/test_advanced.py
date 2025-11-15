"""Advanced Playwright features using Page Object Model"""
from playwright.sync_api import Page, expect
from pages.alerts_page import AlertsPage
from pages.windows_page import WindowsPage
from pages.drag_drop_page import DragDropPage
from pages.hovers_page import HoversPage
from pages.google_page import GooglePage


class TestAdvancedWithPOM:
    """Advanced tests with Page Objects"""
    
    def test_handle_alert(self, page: Page) -> None:
        """Test: Handle alert using page object"""
        alerts_page = AlertsPage(page)
        alerts_page.navigate()
        
        # Setup handler
        alerts_page.setup_alert_handler(action="accept")
        
        # Click button that triggers alert
        alerts_page.click_alert_button()
        
        # Verify result
        result = alerts_page.get_result_text()
        assert "successfully" in result.lower()
    
    def test_dismiss_confirm(self, page: Page) -> None:
        """Test: Dismiss confirm dialog"""
        alerts_page = AlertsPage(page)
        alerts_page.navigate()
        
        # Setup handler to dismiss
        alerts_page.setup_alert_handler(action="dismiss")
        
        # Click confirm button
        alerts_page.click_confirm_button()
        
        # Verify result shows "Cancel"
        result = alerts_page.get_result_text()
        assert "Cancel" in result
    
    def test_prompt_with_text(self, page: Page) -> None:
        """Test: Enter text in prompt"""
        alerts_page = AlertsPage(page)
        alerts_page.navigate()
        
        # Setup handler with text
        alerts_page.setup_alert_handler(text="Hello Playwright!")
        
        # Click prompt button
        alerts_page.click_prompt_button()
        
        # Verify result contains our text
        result = alerts_page.get_result_text()
        assert "Hello Playwright!" in result
    
    def test_multiple_windows(self, page: Page) -> None:
        """Test: Handle multiple windows using page object"""
        windows_page = WindowsPage(page)
        windows_page.navigate()
        
        # Verify original page heading
        assert "Opening a new window" in windows_page.get_page_heading()
        
        # Click link and get new page
        new_page = windows_page.click_new_window_link()
        
        # Verify new window
        expect(new_page).to_have_title('New Window')
        
        # Cleanup
        new_page.close()
    
    def test_drag_and_drop(self, page: Page) -> None:
        """Test: Drag and drop using page object"""
        drag_drop_page = DragDropPage(page)
        drag_drop_page.navigate()
        
        # Verify initial state
        assert drag_drop_page.get_column_a_text() == "A"
        assert drag_drop_page.get_column_b_text() == "B"
        
        # Perform drag and drop
        drag_drop_page.drag_a_to_b()
        
        # Verify columns swapped
        assert drag_drop_page.verify_columns_swapped()
    
    def test_hover_effect(self, page: Page) -> None:
        """Test: Hover effect using page object"""
        hovers_page = HoversPage(page)
        hovers_page.navigate()
        
        # Hover over first figure
        hovers_page.hover_first_figure()
        
        # Caption should appear
        assert hovers_page.is_caption_visible()
        caption_text = hovers_page.get_first_caption_text()
        assert len(caption_text) > 0
    
    def test_mobile_emulation(self, playwright, browser) -> None:
        """Test: Mobile device emulation"""
        # Get iPhone device
        iphone = playwright.devices["iPhone 12"]
        context = browser.new_context(**iphone)
        page = context.new_page()
        
        # Use page object with mobile context
        google_page = GooglePage(page)
        google_page.navigate()
        
        # Verify viewport
        viewport = page.viewport_size
        assert viewport["width"] == 390  # iPhone 12 width
        
        # Verify page loads
        assert google_page.is_search_box_visible()
        
        context.close()
    
    def test_evaluate_javascript(self, page: Page) -> None:
        """Test: Execute JavaScript using page object"""
        google_page = GooglePage(page)
        google_page.navigate()
        
        # Execute JavaScript
        result = page.evaluate("() => document.title")
        
        assert "Google" in result
        assert result == google_page.get_title()