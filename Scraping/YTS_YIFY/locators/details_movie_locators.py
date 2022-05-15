'Locators for the DETAILS (name of the book, link of the book, price of the book, rating of the book) for every book (GROUP)'

class DetailsMovieLocators:
    """
    Locators in Details Page for properties of a movie
    """
    DETAILS_PAGE_MOVIE_NAME_LOCATOR = 'div.main-content div.container div.hidden-xs h1'
    #DETAILS_PAGE_MOVIE_NAME_LOCATOR = '#movie-info > div.hidden-xs > h1'
    DETAILS_PAGE_MOVIE_YEAR_LOCATOR = 'div.main-content div.container div.hidden-xs h2:nth-child(2)'
    DETAILS_PAGE_MOVIE_GENRE_LOCATOR = 'div.main-content div.container div.hidden-xs h2:nth-child(3)'
    DETAILS_PAGE_MOVIE_TORRENT_LOCATOR = 'div.main-content div.container p.hidden-xs.hidden-sm a:nth-child(3)'
    DETAILS_PAGE_MOVIE_IMDB_LINK_LOCATOR = 'div.main-content div.container div.bottom-info a[href*="imdb"]'
    DETAILS_PAGE_MOVIE_IMAGE_LOCATOR = 'to be completed...'
