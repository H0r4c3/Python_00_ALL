from bs4 import BeautifulSoup

from parser_details import ParserDetails



class AllParagraphsForParsing:
    def __init__(self, page, PARAGRAPHS_locator, DETAIL_locator):
        self.soup = BeautifulSoup(page, 'html.parser')
        self.PARAGRAPHS_locator = PARAGRAPHS_locator
        self.DETAIL_locator = DETAIL_locator
        self.paragraphs_list = []

    def __repr__(self):
        return f'\n\n Start PARAGRAPH: \n {self.paragraphs_list[0]} \n End PARAGRAPH \n\n'

    @property
    def allparagraphs(self):
        self.paragraphs_list = self.soup.select(self.PARAGRAPHS_locator)
        #print(self.paragraphs_list)
        return [ParserDetails(e, self.DETAIL_locator) for e in self.paragraphs_list]

    