import re

from locators.details_movie_locators import DetailsMovieLocators

#logger = logging.getLogger('scraping.book_parser')


class DetailsMovieParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    def __init__(self, parent):
        self.parent = parent # parent's locator = div.browse-movie-wrap.col-xs-10.col-sm-5>

    def __repr__(self):
        return f'<Movie: {self.name} IMDB: {self.imdb_link} Year: {self.year} Genre: {self.genre} Torrent: {self.torrent}>'

    @property
    def name(self):
        locator = DetailsMovieLocators.MOVIE_NAME_LOCATOR
        item_name = self.parent.select_one(locator).string
        return item_name

    @property
    def imdb_link(self):
        locator = DetailsMovieLocators.IMDB_LINK_LOCATOR
        imdb_link = self.parent.select_one(locator).attrs['href']
        return imdb_link

    @property
    def torrent(self):
        locator = DetailsMovieLocators.TORRENT_LOCATOR
        torrent = self.parent.select_one(locator).string
        return torrent

    @property
    def year(self):
        locator = DetailsMovieLocators.YEAR_LOCATOR
        year = self.parent.select_one(locator).string
        return year

    @property
    def genre(self):
        locator = DetailsMovieLocators.GENRE_LOCATOR
        genre = self.parent.select_one(locator).string
        return genre
