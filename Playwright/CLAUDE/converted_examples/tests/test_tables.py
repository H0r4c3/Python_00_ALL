"""Table tests using Page Object Model"""
from playwright.sync_api import Page
from pages.tables_page import TablesPage


class TestTablesWithPOM:
    """Table tests with Page Objects"""
    
    def test_count_table_rows(self, page: Page) -> None:
        """Test: Count rows using page object"""
        tables_page = TablesPage(page)
        tables_page.navigate()
        
        count = tables_page.get_rows_count()
        assert count > 0
    
    def test_get_first_cell_text(self, page: Page) -> None:
        """Test: Get cell text using page object"""
        tables_page = TablesPage(page)
        tables_page.navigate()
        
        text = tables_page.get_first_cell_text()
        assert len(text) > 0
    
    def test_get_nth_row(self, page: Page) -> None:
        """Test: Get specific row using page object"""
        tables_page = TablesPage(page)
        tables_page.navigate()
        
        third_row_text = tables_page.get_nth_row_text(2)
        assert len(third_row_text) > 0
    
    def test_filter_rows_by_text(self, page: Page) -> None:
        """Test: Filter rows using page object"""
        tables_page = TablesPage(page)
        tables_page.navigate()
        
        # Filter rows containing any common text
        count = tables_page.filter_rows_by_text("$")
        assert count > 0