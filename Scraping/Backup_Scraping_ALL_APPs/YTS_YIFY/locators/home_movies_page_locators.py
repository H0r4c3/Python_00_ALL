

class HomeMoviesPageLocators:
    """
    Locators for the GROUPs of movies from Home page (Group of Popular movies, Group of Latest movies, Group of Upcoming movies)
    """
    POPULAR_MOVIES_LOCATOR = 'div.main-content div#popular-downloads div.browse-movie-wrap.col-xs-10.col-sm-5'

    POPULAR_TITLE = 'a.browse-movie-title'
    POPULAR_YEAR = 'div.browse-movie-year'
    POPULAR_TORRENT = 'div.browse-movie-bottom div.browse-movie-tags a[title*="1080"]'
    #POPULAR_TORRENT = 'div.browse-movie-bottom div.browse-movie-tags a'
    POPULAR_IMAGE = 'img.img-responsive'

    DETAILS_PAGE_PATH = 'a.browse-movie-link'


    LATEST_MOVIES_LOCATOR = 'div.main-content div.content-dark div.home-movies div.browse-movie-wrap.col-xs-10.col-sm-5'


    #UPCOMING_MOVIES_LOCATOR = 'div.main-content div.home-movies:nth-child(2) div.browse-movie-wrap.col-xs-10.col-sm-5'
    UPCOMING_MOVIES_LOCATOR = 'body > div.main-content > div:nth-child(6) > div > div:nth-child(2) > div'
