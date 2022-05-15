from bs4 import BeautifulSoup



class AllParagraphsForParsing:
    def __init__(self, page_content, PARAGRAPHS_locator):
        self.soup = BeautifulSoup(page_content, 'html.parser')
        self.PARAGRAPHS_locator = PARAGRAPHS_locator
        self.paragraphs_list = []

    def __repr__(self):
        return f'\n\n Start PARAGRAPH: \n {self.paragraphs_list[0]} \n End PARAGRAPH \n\n'

    @property
    def allparagraphs(self):
        #PARAGRAPHS_locator = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
        self.paragraphs_list = self.soup.select(self.PARAGRAPHS_locator)
        #print(self.paragraphs_list[0])
        #return [ParserDetails(e, self.DETAIL_locator) for e in self.paragraphs_list]
        return self.paragraphs_list