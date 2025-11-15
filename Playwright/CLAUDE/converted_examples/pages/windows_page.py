"""Multiple windows page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class WindowsPage(BasePage):
    """Windows/tabs page"""
    
    URL = "https://the-internet.herokuapp.com/windows"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.click_here_link = page.locator("a:has-text('Click Here')")
    
    def navigate(self) -> None:
        """Navigate to windows page"""
        self.navigate_to(self.URL)
    
    def click_new_window_link(self):
        """Click link that opens new window and return new page"""
        with self.page.expect_popup() as popup_info:
            self.click_here_link.click()
        return popup_info.value
    
    def get_page_heading(self) -> str:
        """Get page heading text"""
        return self.page.locator("h3").inner_text()