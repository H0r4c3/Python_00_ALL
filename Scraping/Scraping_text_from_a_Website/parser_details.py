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
        return f'Details:\n {self.detail}'

    @property
    def detail(self):
        #DETAIL_LOCATOR = 'article.product_pod h3 a'
        if self.parent.select_one(self.DETAIL_locator) != None:
            #item_details = self.parent.select_one(self.DETAIL_locator).attrs['title']
            all_text_string = self.parent.select_one(self.DETAIL_locator).text
            list_of_words = all_text_string.split() # eliminate the multiple spaces and creates a list of words
            item_details_string = ' '.join(list_of_words) # creates a string from all the words, having a space between them
            item_details = item_details_string
            return item_details
        else:
            item_details = 'None'
            #print("No title found!")
            return item_details

    def convert_list_of_strings_to_a_string(self, list_of_strings):
        full_str = ' '.join([str(item) for item in list_of_strings])

        return full_str

    def add_new_line_char(self, list_of_words):
        list_of_words_new_line = [substring.replace('.', '.\n') for substring in list_of_words]
        return list_of_words_new_line