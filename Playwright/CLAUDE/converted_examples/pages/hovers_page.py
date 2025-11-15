"""Hovers page object"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class HoversPage(BasePage):
    """Hovers page"""
    
    URL = "https://the-internet.herokuapp.com/hovers"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.figures = page.locator("div.figure")
        self.captions = page.locator(".figcaption")
    
    def navigate(self) -> None:
        """Navigate to hovers page"""
        self.navigate_to(self.URL)
    
    def hover_first_figure(self) -> None:
        """Hover over first figure"""
        self.figures.first.hover()
    
    def hover_nth_figure(self, n: int) -> None:
        """Hover over nth figure"""
        self.figures.nth(n).hover()
    
    def is_caption_visible(self) -> bool:
        """Check if caption is visible"""
        return self.captions.first.is_visible()
    
    def get_first_caption_text(self) -> str:
        """Get first caption text"""
        return self.captions.first.inner_text()