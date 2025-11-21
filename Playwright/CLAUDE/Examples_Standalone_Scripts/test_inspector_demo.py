"""Demo: How to use Playwright Inspector"""
import pytest
#from pages.practice_store_page import PracticeStorePage
from playwright.sync_api import Page, expect


class TestInspectorDemo:
    
    def test_find_search_elements(self, page: Page):
        """Use Inspector to find search elements"""
        page.goto("https://practicesoftwaretesting.com/")
        
        # Inspector opens here!
        page.pause()
        
        print("\n🔍 Inspector will open now...")
        print("Click 'Pick Locator' and hover over the search box")
        
        # After you find the test ID, write your test:
        page.get_by_test_id("search-query").fill("hammer")
        page.get_by_test_id("search-submit").click()
        
        # Pause again to see results
        page.pause()