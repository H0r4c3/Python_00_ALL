'Locators for the DETAILS (name of the book, link of the book, price of the book, rating of the book) for every book (GROUP)'

class ImdbLocators:
    """
    Locators in IMDB Page for a movie
    """
    IMDB_NAME_LOCATOR = ''
    IMDB_YEAR_LOCATOR = ''
    IMDB_GENRE_LOCATOR = ''
    
    IMDB_IMAGE_LOCATOR = ''

    #IMDB_RATING_LOCATOR = '#main > class.titlereference-header > ul.ipl-inline-list > div.ipl-rating-star > span.ipl-rating-star__rating'
    IMDB_RATING_LOCATOR = 'span.ipl-rating-star__rating'
    #IMDB_NR_OF_VOTES_LOCATOR = '#main > class.titlereference-header > ul.ipl-inline-list > div.ipl-rating-star > span.ipl-rating-star__total-votes'
    IMDB_NR_OF_VOTES_LOCATOR = 'span.ipl-rating-star__total-votes'