'Locators for the DETAILS (name of the book, link of the book, price of the book, rating of the book) for every book (GROUP)'

class BookLocators:
    """
    Locators for an item in the HTML page.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'