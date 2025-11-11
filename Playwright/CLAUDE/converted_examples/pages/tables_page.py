"""Tables page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class TablesPage(BasePage):
    """Tables page"""
    
    URL = "https://the-internet.herokuapp.com/tables"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.table = page.locator("table")
        self.rows = page.locator("table tr")
        self.cells = page.locator("table td")
    
    def navigate(self) -> None:
        """Navigate to tables page"""
        self.navigate_to(self.URL)
    
    def get_rows_count(self) -> int:
        """Get number of rows"""
        return self.rows.count()
    
    def get_first_cell_text(self) -> str:
        """Get text of first cell"""
        return self.cells.first.inner_text()
    
    def get_nth_row_text(self, n: int) -> str:
        """Get text of nth row"""
        return self.rows.nth(n).inner_text()
    
    def get_last_row_text(self) -> str:
        """Get text of last row"""
        return self.rows.last.inner_text()
    
    def filter_rows_by_text(self, text: str) -> int:
        """Filter rows containing text and return count"""
        return self.rows.filter(has_text=text).count()