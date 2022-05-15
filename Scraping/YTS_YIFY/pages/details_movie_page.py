
'https://learning.oreilly.com/videos/the-complete-python/9781839217289/9781839217289-video11_17'

import re

from bs4 import BeautifulSoup

from locators.details_movie_locators import DetailsMovieLocators

#logger = logging.getLogger('scraping.all_books_page')

class DetailsMoviePage:
    """
    The details page for a movie
    """
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    def __repr__(self):
        return f'\n Movie_from_details_page: {self.name_from_details_page} | Year: {self.year_from_details_page} |  Genre: {self.genre_from_details_page} | Quality: {self.quality_from_details_page} |Torrent: {self.torrent_from_details_page} | IMDB: {self.imdb_link_from_details_page} | IMDB Rating: {self.rating_from_imdb_page} | IMDB Votes: {self.nr_of_votes_from_imdb_page}' 

    @property
    def name_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_NAME_LOCATOR
        if self.soup.select_one(locator) != None:
            item_name = self.soup.select_one(locator).string
        else:
            item_name = 'None'
            #print("No title found in details page!")
        return item_name

    @property
    def year_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_YEAR_LOCATOR
        if self.soup.select_one(locator) != None:
            item_year = self.soup.select_one(locator).string
        else:
            item_year = 'None'
            #print("No year found in details page!")
        return item_year

    @property
    def genre_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_GENRE_LOCATOR
        if self.soup.select_one(locator) != None:
            item_genre = self.soup.select_one(locator).string
        else:
            item_genre = 'None'
            #print("No genre found in details page!")
        return item_genre

    @property
    def quality_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_TORRENT_LOCATOR
        if self.soup.select_one(locator) != None:
            item_quality = self.soup.select_one(locator).string
        else:
            item_quality = 'None'
            #print("No quality found in details page!")
        return item_quality

    @property
    def torrent_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_TORRENT_LOCATOR
        if self.soup.select_one(locator) != None:
            item_torrent = self.soup.select_one(locator).attrs['href']
        else:
            item_torrent = 'None'
            #print("No torrent found in details page!")
        return item_torrent

    @property
    def imdb_link_from_details_page(self):
        locator = DetailsMovieLocators.DETAILS_PAGE_MOVIE_IMDB_LINK_LOCATOR
        if self.soup.select_one(locator) != None:
            item_imdb_link = self.soup.select_one(locator).attrs['href']
        else:
            item_imdb_link = 'https://www.imdb.com/title/tt0111161/'
            #print("No imdb link found in details page!")
        return item_imdb_link

    

    

    

    