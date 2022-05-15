from bs4 import BeautifulSoup

from day_page_parser import DayPageParser
from locators.DAY_Locators import DayLocators


class DayPage:
    """
    # pagina cu randuri pentru fiecare ora
    """
    def __init__(self, content_page):
        self.soup = BeautifulSoup(content_page, 'html.parser')

    @property
    def rows_with_ore_in_day_page(self):
        return [DayPageParser(e) for e in self.soup.select(DayLocators.row_with_ore_LOCATOR)]

    @property
    def rows_with_locuri_in_day_page(self):
        return [DayPageParser(e) for e in self.soup.select(DayLocators.row_with_locuri_LOCATOR)]

    @property
    def data_in_day_page(self):
        return [DayPageParser(e) for e in [self.soup.select_one(DayLocators.data1_LOCATOR)]]



