from playwright.sync_api import Page, expect
from ChatGPT.Example.pages.homepage_page import HomePage


class TestHomepage:
    """Test suite for homepage functionality."""

    def test_title_is_correct(self, page: Page):
        """Verify homepage title is correct."""
        home = HomePage(page)
        home.open()
        expect(page).to_have_title("Practice Software Testing - Toolshop - v5.0")

    def test_logo_is_visible(self, page: Page):
        """Verify logo is visible."""
        home = HomePage(page)
        home.open()
        home.assert_home_loaded()

    def test_search_functionality(self, page: Page):
        """Verify search box works."""
        home = HomePage(page)
        home.open()
        home.search("keyboard")
        expect(page).to_have_url("**/search")
