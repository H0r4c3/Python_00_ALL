"""Dropdown page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Dropdown page"""
    
    URL = "https://the-internet.herokuapp.com/dropdown"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.dropdown = page.locator("select#dropdown")
    
    def navigate(self) -> None:
        """Navigate to dropdown page"""
        self.navigate_to(self.URL)
    
    def select_option(self, value: str) -> None:
        """Select dropdown option by value"""
        self.dropdown.select_option(value)
    
    def get_selected_value(self) -> str:
        """Get currently selected value"""
        return self.dropdown.input_value()
    
    def get_selected_text(self) -> str:
        """Get currently selected text"""
        return self.dropdown.locator("option:checked").inner_text()