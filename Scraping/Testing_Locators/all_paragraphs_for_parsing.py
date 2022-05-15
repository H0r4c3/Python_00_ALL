from bs4 import BeautifulSoup

from parser_details import ParserDetails



class AllParagraphsForParsing:
    def __init__(self, page, PARAGRAPHS_locator, DETAIL_locator):
        self.soup = BeautifulSoup(page, 'html.parser')
        #self.soup.prettify()
        self.PARAGRAPHS_locator = PARAGRAPHS_locator
        self.DETAIL_locator = DETAIL_locator
        self.paragraphs_list = []

    def __repr__(self):
        #return f'\n\n Start PARAGRAPH: \n {self.paragraphs_list[0]} \n End PARAGRAPH \n\n'
        return f'\n\n Start PARAGRAPH: \n {self.allparagraphs} \n End PARAGRAPH \n\n'

    @property
    def allparagraphs(self):
        #PARAGRAPHS_locator = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
        self.paragraphs_list = self.soup.select(self.PARAGRAPHS_locator)
        print('\n\n Start PARAGRAPH: \n', self.paragraphs_list[0], '\n End PARAGRAPH \n\n')
        return [ParserDetails(e, self.DETAIL_locator) for e in self.paragraphs_list]

    