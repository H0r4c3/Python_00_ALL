"""Page Object for Practice Software Testing store"""
from playwright.sync_api import Page
from .base_page import BasePage


class PracticeStorePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://practicesoftwaretesting.com"
        
        # Locators for the practice store
        self.search_input = 'input[data-test="search-query"]'
        self.search_button = 'button[data-test="search-submit"]'
        self.product_cards = '[data-test="product-card"]'
        self.product_names = '[data-test="product-name"]'
    
    def navigate(self):
        """Navigate to practice store"""
        self.page.goto(self.url)
        self.page.wait_for_load_state('networkidle')
    
    def search(self, query: str):
        """Search for products"""
        self.page.fill(self.search_input, query)
        self.page.click(self.search_button)
        self.page.wait_for_load_state('networkidle')
    
    def get_product_count(self) -> int:
        """Get number of products displayed"""
        return self.page.locator(self.product_cards).count()
    
    def get_product_names(self) -> list[str]:
        """Get all visible product names"""
        return self.page.locator(self.product_names).all_text_contents()
    
    def click_product(self, index: int = 0):
        """Click on a product by index"""
        self.page.locator(self.product_cards).nth(index).click()