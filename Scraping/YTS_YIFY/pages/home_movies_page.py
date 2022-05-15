'https://learning.oreilly.com/videos/the-complete-python/9781839217289/9781839217289-video11_17'

import re

from bs4 import BeautifulSoup

from locators.home_movies_page_locators import HomeMoviesPageLocators
from parsers.home_movies_parser import HomeMoviesParser

#logger = logging.getLogger('scraping.all_books_page')

class HomeMoviesPage:
    """
    In the Home page, this class groups the movies in 3 groups: Popular, Latest, Upcoming
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def popular_movies(self):
        return [HomeMoviesParser(e) for e in self.soup.select(HomeMoviesPageLocators.POPULAR_MOVIES_LOCATOR)]


    @property
    def latest_movies(self):
        return [HomeMoviesParser(e) for e in self.soup.select(HomeMoviesPageLocators.LATEST_MOVIES_LOCATOR)]


    @property
    def upcoming_movies(self):
        return [HomeMoviesParser(e) for e in self.soup.select(HomeMoviesPageLocators.UPCOMING_MOVIES_LOCATOR)]


