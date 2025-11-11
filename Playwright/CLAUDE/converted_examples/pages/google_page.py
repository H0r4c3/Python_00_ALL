"""Google search page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class GooglePage(BasePage):
    """Google search page"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_box = page.locator("textarea[name='q']")
        self.search_button = page.locator("input[name='btnK']")
        self.results = page.locator("h3")
    
    def navigate(self) -> None:
        """Navigate to Google"""
        self.navigate_to("https://www.google.com")
    
    def search(self, query: str) -> None:
        """Perform search"""
        self.search_box.fill(query)
        self.search_box.press("Enter")
    
    def get_first_result_text(self) -> str:
        """Get first result text"""
        return self.results.first.inner_text()
    
    def get_results_count(self) -> int:
        """Get number of results"""
        return self.results.count()
    
    def is_search_box_visible(self) -> bool:
        """Check if search box is visible"""
        return self.search_box.is_visible()