"""Checkboxes page object"""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    """Checkboxes page"""
    
    URL = "https://the-internet.herokuapp.com/checkboxes"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkboxes = page.locator("input[type='checkbox']")
    
    def navigate(self) -> None:
        """Navigate to checkboxes page"""
        self.navigate_to(self.URL)
    
    def check_first_checkbox(self) -> None:
        """Check first checkbox"""
        self.checkboxes.first.check()
    
    def uncheck_checked_checkbox(self) -> None:
        """Uncheck first checked checkbox"""
        checked = self.page.locator("input[type='checkbox']:checked")
        if checked.count() > 0:
            checked.first.uncheck()
    
    def is_first_checkbox_checked(self) -> bool:
        """Check if first checkbox is checked"""
        return self.checkboxes.first.is_checked()
    
    def get_checkboxes_count(self) -> int:
        """Get number of checkboxes"""
        return self.checkboxes.count()