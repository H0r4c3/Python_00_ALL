"""Base page class with common functionality"""
from playwright.sync_api import Page


class BasePage:
    """Base page that all page objects inherit from"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, url: str) -> None:
        """Navigate to URL"""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get current URL"""
        return self.page.url
    
    def screenshot(self, path: str) -> None:
        """Take screenshot"""
        self.page.screenshot(path=path)