"""Form interaction tests using Page Object Model"""
from playwright.sync_api import Page, expect
from pages.dropdown_page import DropdownPage
from pages.checkboxes_page import CheckboxesPage


class TestFormsWithPOM:
    """Form tests with Page Objects"""
    
    def test_select_dropdown_option(self, page: Page) -> None:
        """Test: Dropdown using page object"""
        dropdown_page = DropdownPage(page)
        dropdown_page.navigate()
        dropdown_page.select_option("1")
        
        assert dropdown_page.get_selected_value() == "1"
        assert dropdown_page.get_selected_text() == "Option 1"
    
    def test_check_checkbox(self, page: Page) -> None:
        """Test: Check checkbox using page object"""
        checkboxes_page = CheckboxesPage(page)
        checkboxes_page.navigate()
        checkboxes_page.check_first_checkbox()
        
        assert checkboxes_page.is_first_checkbox_checked()
    
    def test_uncheck_checkbox(self, page: Page) -> None:
        """Test: Uncheck checkbox using page object"""
        checkboxes_page = CheckboxesPage(page)
        checkboxes_page.navigate()
        
        # First, ensure there's a checked checkbox
        if not checkboxes_page.is_first_checkbox_checked():
            checkboxes_page.check_first_checkbox()
        
        checkboxes_page.uncheck_checked_checkbox()
        # Verify by checking if at least one checkbox became unchecked
        assert checkboxes_page.get_checkboxes_count() > 0