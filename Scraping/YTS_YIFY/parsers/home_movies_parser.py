import re

from locators.home_movies_page_locators import HomeMoviesPageLocators

from pages.details_movie_page import DetailsMoviePage

#logger = logging.getLogger('scraping.book_parser')


class HomeMoviesParser:
    """
    A class for extracting the details for every movie from Home page
    """

    def __init__(self, parent):
        self.parent = parent # parent's locator = div.browse-movie-wrap.col-xs-10.col-sm-5>

    def __repr__(self):
        return f'\n Movie_from_home_or_browse_page: {self.name_home} | Year: {self.year_home} | Quality: {self.quality_home} | Torrent: {self.torrent_home} | Details_Page_Path: {self.details_page_path} | Img_Path: {self.image_home}'

    @property
    def name_home(self):
        locator = HomeMoviesPageLocators.POPULAR_TITLE
        if self.parent.select_one(locator) != None:
            item_name = self.parent.select_one(locator).string
        else:
            item_name = 'None'
            #print("No title found!")
        return item_name

    @property
    def year_home(self):
        locator = HomeMoviesPageLocators.POPULAR_YEAR
        if self.parent.select_one(locator) != None:
            item_year = self.parent.select_one(locator).string
        else:
            item_year = 'None'
            #print("No year found!")
        return item_year

    @property
    def quality_home(self):
        locator = HomeMoviesPageLocators.POPULAR_TORRENT
        if self.parent.select_one(locator) != None:
            item_quality = self.parent.select_one(locator).string
        else:
            item_quality = 'None'
            #print("No 1080 quality found!")
        return item_quality

    @property
    def torrent_home(self):
        locator = HomeMoviesPageLocators.POPULAR_TORRENT
        if self.parent.select_one(locator) != None:
            item_torrent = self.parent.select_one(locator).attrs['href']
        else:
            item_torrent = 'None'
            #print("No 1080 torrent found!")
        return item_torrent

    @property
    def details_page_path(self):
        locator = HomeMoviesPageLocators.DETAILS_PAGE_PATH
        if self.parent.select_one(locator) != None:
            item_details_page_path = self.parent.select_one(locator).attrs['href']
        else:
            item_details_page_path = 'https://yts.mx/movies/the-shawshank-redemption-1994'
            #print("No details page path")
        return item_details_page_path


    @property
    def image_home(self):
        locator = HomeMoviesPageLocators.POPULAR_IMAGE
        if self.parent.select_one(locator) != None:
            item_image = self.parent.select_one(locator).attrs['src']
            path_item_image = item_image
        else:
            item_image = 'None'
            #print("No image for this movie!")
            path_item_image = default_path # to be added a default img for movies without images
        return path_item_image

    




    