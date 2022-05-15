
'https://learning.oreilly.com/videos/the-complete-python/9781839217289/9781839217289-video11_17'

import re
import logging

from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser

#logger = logging.getLogger('scraping.all_books_page')

class AllBooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
