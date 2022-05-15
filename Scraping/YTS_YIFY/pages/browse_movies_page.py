
'https://learning.oreilly.com/videos/the-complete-python/9781839217289/9781839217289-video11_17'

import re

from bs4 import BeautifulSoup

from locators.browse_movies_locator import BrowseMoviesLocator
from parsers.home_movies_parser import HomeMoviesParser

#logger = logging.getLogger('scraping.all_books_page')

class BrowseMoviesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def browse_movies(self):
        return [HomeMoviesParser(e) for e in self.soup.select(BrowseMoviesLocator.BROWSE_MOVIES_LOCATOR)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllMoviesPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
