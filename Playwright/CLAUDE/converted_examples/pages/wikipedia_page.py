"""Wikipedia page object for navigation tests"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class WikipediaPage(BasePage):
    """Wikipedia page"""
    
    URL = "https://www.wikipedia.org"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator("#searchInput")
        self.main_heading = page.locator("h1")
        self.footer = page.locator("footer")
    
    def navigate(self) -> None:
        """Navigate to Wikipedia"""
        self.navigate_to(self.URL)
    
    def search(self, query: str) -> None:
        """Perform search"""
        self.search_input.fill(query)
        self.search_input.press("Enter")
    
    def is_on_wikipedia(self) -> bool:
        """Check if on Wikipedia"""
        return "wikipedia" in self.get_url().lower()
    
    def scroll_to_footer(self) -> None:
        """Scroll footer into view"""
        self.footer.scroll_into_view_if_needed()
    
    def is_footer_visible(self) -> bool:
        """Check if footer is visible"""
        return self.footer.is_visible()