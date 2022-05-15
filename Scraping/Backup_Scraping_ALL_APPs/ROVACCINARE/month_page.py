from bs4 import BeautifulSoup

from month_page_parser import MonthPageParser

from locators.MONTH_Locators import MonthLocators

#logger = logging.getLogger('scraping.all_books_page')

class MonthPage:
    """
    # pagina cu calendarul pentru o luna, fiecare celula e o zi
    """
    def __init__(self, content_page):
        self.soup = BeautifulSoup(content_page, 'html.parser')

    @property
    def cells_in_month_page(self):
        return [MonthPageParser(e) for e in self.soup.select(MonthLocators.Calendar_Month_Cell_LOCATOR)]



