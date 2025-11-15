"""Drag and drop page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class DragDropPage(BasePage):
    """Drag and drop page"""
    
    URL = "https://the-internet.herokuapp.com/drag_and_drop"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.column_a = page.locator("#column-a")
        self.column_b = page.locator("#column-b")
    
    def navigate(self) -> None:
        """Navigate to drag and drop page"""
        self.navigate_to(self.URL)
    
    def drag_a_to_b(self) -> None:
        """Drag column A to column B"""
        self.page.drag_and_drop("#column-a", "#column-b")
    
    def get_column_a_text(self) -> str:
        """Get column A header text"""
        return self.column_a.inner_text()
    
    def get_column_b_text(self) -> str:
        """Get column B header text"""
        return self.column_b.inner_text()
    
    def verify_columns_swapped(self) -> bool:
        """Verify columns have swapped"""
        return self.get_column_a_text() == "B" and self.get_column_b_text() == "A"