"""JavaScript alerts page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class AlertsPage(BasePage):
    """JavaScript alerts page"""
    
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.alert_button = page.locator("button:has-text('Click for JS Alert')")
        self.confirm_button = page.locator("button:has-text('Click for JS Confirm')")
        self.prompt_button = page.locator("button:has-text('Click for JS Prompt')")
        self.result = page.locator("#result")
    
    def navigate(self) -> None:
        """Navigate to alerts page"""
        self.navigate_to(self.URL)
    
    def click_alert_button(self) -> None:
        """Click button that triggers alert"""
        self.alert_button.click()
    
    def click_confirm_button(self) -> None:
        """Click button that triggers confirm"""
        self.confirm_button.click()
    
    def click_prompt_button(self) -> None:
        """Click button that triggers prompt"""
        self.prompt_button.click()
    
    def get_result_text(self) -> str:
        """Get result text"""
        return self.result.inner_text()
    
    def setup_alert_handler(self, action: str = "accept", text: str = None) -> None:
        """
        Setup handler for dialog
        action: 'accept' or 'dismiss'
        text: text to enter in prompt
        """
        def handle_dialog(dialog):
            if text:
                dialog.accept(text)
            elif action == "accept":
                dialog.accept()
            else:
                dialog.dismiss()
        
        self.page.on("dialog", handle_dialog)