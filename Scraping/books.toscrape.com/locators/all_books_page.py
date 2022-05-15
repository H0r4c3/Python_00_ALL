'''
BOOKS = Locator for the GROUPs with all the details (name of the book, link of the book, price of the book, rating of the book) in page 1 (Group for book1, Group for book2 etc)
'''

class AllBooksPageLocators:
    BOOKS = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
    PAGER = 'div.page_inner section ul.pager li.current'
