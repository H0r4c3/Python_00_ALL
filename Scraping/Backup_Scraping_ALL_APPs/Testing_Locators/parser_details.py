#import APP_scraper

class ParserDetails:
    """
    A class for extracting the details for every movie from Home page
    """

    def __init__(self, parent, DETAIL_locator):
        self.parent = parent # parent's locator = div.browse-movie-wrap.col-xs-10.col-sm-5>
        self.DETAIL_locator = DETAIL_locator
        self.item_details = ''

    def __repr__(self):
        return f'\n Details: {self.detail_without_text}'

    @property
    def details(self):
        #DETAIL_LOCATOR = 'article.product_pod h3 a'
        if self.parent.select_one(self.DETAIL_locator) != None:
            #item_details = self.parent.select_one(self.DETAIL_locator).attrs['title']
            all_text_string = self.parent.select_one(self.DETAIL_locator).text
            list_of_words = all_text_string.split() # eliminate the multiple spaces and creates a list of words
            item_details_string = ' '.join(list_of_words) # creates a string from all the words, having a space between them
            return item_details_string
        else:
            item_details_string = 'None'
            #print("No title found!")
            return item_details_string

    @property
    def detail_without_text(self):
        #DETAIL_LOCATOR = 'article.product_pod h3 a'
        if self.parent.select_one(self.DETAIL_locator) != None:
            #item_details = self.parent.select_one(self.DETAIL_locator).attrs['title']
            try:
                item_detail_string = self.parent.select_one(self.DETAIL_locator)
            except Exception as e:
                print("Wrong locator!!!")
                item_detail_string = 'None'
            #list_of_words = all_text_string.split() # eliminate the multiple spaces and creates a list of words
            #item_details_string = ' '.join(list_of_words) # creates a string from all the words, having a space between them
            return item_detail_string
        else:
            item_detail_string = 'None'
            #print("No title found!")
            return item_detail_string
    