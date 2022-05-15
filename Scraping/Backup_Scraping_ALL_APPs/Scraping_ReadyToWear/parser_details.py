#import APP_scraper

class ParserDetails:
    """
    A class for extracting the details for every movie from Home page
    """

    def __init__(self, parent, DETAIL_locator):
        self.parent = parent # parent's locator = div.browse-movie-wrap.col-xs-10.col-sm-5>
        self.DETAIL_locator = DETAIL_locator
        self.list_of_details = []

    def __repr__(self):
        return f'Details:\n {self.detail}'

    @property
    def detail(self):
        #DETAIL_LOCATOR = 'article.product_pod h3 a'
        if self.parent.select_one(self.DETAIL_locator) != None:
            #item_detail = self.parent.select_one(self.DETAIL_locator).attrs['title']
            item_detail = self.parent.select_one(self.DETAIL_locator).text
            item_details_string = ' '.join(item_detail.split())
            print(item_details_string)
            item_details_list = item_detail.split()
            item_detail = self.modify_string(item_details_list)
            #item_detail = item_details_string
        else:
            item_detail = 'None'
            #print("No title found!")
        return item_detail

    def modify_string(self, item_detail_list):
 
        self.list_of_details.append(item_detail_list[0] + ' ' + item_detail_list[1])
        self.list_of_details.append(item_detail_list[2] + ' ' + item_detail_list[3] + ' ' + item_detail_list[4])
        self.list_of_details.append(item_detail_list[5] + ' ' + item_detail_list[6] + ' '  + item_detail_list[7] + ' ' + item_detail_list[8] + ' ' + item_detail_list[9] + ' ' + item_detail_list[10] + ' ' + item_detail_list[11])
        self.list_of_details.append(item_detail_list[12] + ' ' + item_detail_list[13] + ' ' + item_detail_list[14] + ' ' + item_detail_list[15] + ' ' + item_detail_list[16])
        self.list_of_details.append(item_detail_list[18] + ' ' + item_detail_list[22] + ' ' + item_detail_list[23] + ' ' + item_detail_list[24] + ' ' +  item_detail_list[25])

        return self.list_of_details

    def convert_list_of_strings_to_a_string(self, list_of_strings):
        full_str = ' '.join([str(item) for item in list_of_strings])

        return full_str
        

    def modify_string2(self, item_detail_list):
 
        self.list_of_details.append(item_detail_list[0] + ' ' + item_detail_list[1])
        self.list_of_details.append(item_detail_list[2] + ' ' + item_detail_list[3] + ' ' + item_detail_list[4])
        self.list_of_details.append(item_detail_list[5] + ' ' + item_detail_list[6] + ' '  + item_detail_list[7] + ' ' + item_detail_list[8] + ' ' + item_detail_list[9] + ' ' + item_detail_list[10] + ' ' + item_detail_list[11])
        self.list_of_details.append(item_detail_list[12] + ' ' + item_detail_list[13] + item_detail_list[14] + item_detail_list[15])
        self.list_of_details.append(item_detail_list[17] + item_detail_list[21] + item_detail_list[22] + item_detail_list[23] +  item_detail_list[24])

        return self.list_of_details

    def add_new_line_char(self, item_detail_list):
        item_detail_list[1] = item_detail_list[1] + '\n'
        item_detail_list[4] = item_detail_list[4] + '\n'
        item_detail_list[11] = item_detail_list[11] + '\n'
        item_detail_list[15] = item_detail_list[15] + '\n'
        item_detail_list[24] = item_detail_list[24] + '\n'