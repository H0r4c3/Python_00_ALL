
'https://learning.oreilly.com/videos/the-complete-python/9781839217289/9781839217289-video11_17'

import re

from bs4 import BeautifulSoup

from locators.details_movie_locators import DetailsMovieLocators
from locators.imdb_locators import ImdbLocators

#logger = logging.getLogger('scraping.all_books_page')

class ImdbPage:
    """
    The IMDB page for a movie
    """
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    def __repr__(self):
        return f'\n Movie_from_details_page: {self.name_from_details_page} | IMDB: {self.imdb_link_from_details_page} | IMDB Rating: {self.rating_from_imdb_page} | IMDB Votes: {self.nr_of_votes_from_imdb_page}' 

    @property
    def rating_from_imdb_page(self):
        locator = ImdbLocators.IMDB_RATING_LOCATOR
        if self.soup.select_one(locator) != None:
            item_rating_from_imdb_page = self.soup.select_one(locator).string
        else:
            item_rating_from_imdb_page = 'None'
            print("No title found in details page!")
        return item_rating_from_imdb_page

    @property
    def nr_of_votes_from_imdb_page(self):
        locator = ImdbLocators.IMDB_NR_OF_VOTES_LOCATOR
        if self.soup.select_one(locator) != None:
            item_nr_of_votes_from_imdb_page = self.soup.select_one(locator).string
        else:
            item_nr_of_votes_from_imdb_page = 'None'
            print("No year found in details page!")
        return item_nr_of_votes_from_imdb_page


    

    

    

    

    