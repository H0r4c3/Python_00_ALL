from bs4 import BeautifulSoup
import requests

#logger = logging.getLogger('scraping.all_books_page')

class ScrapingHTML:
    """
    Giving an html file, scraping some values
    """
    def __init__(self, path):
        self.path = path
        #self.locator = locator
        file_content = open(path)
        self.soup = BeautifulSoup(file_content, 'html.parser')
        file_content.close()
        

    def scraping(self, locator):
        if self.soup.select_one(locator) != None:
            item_value = self.soup.select_one(locator).text
        else:
            item_value = None
        return item_value

def main():
    path = "C:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Check_Values_in_Two_Files/Test_Result03AB.html"

    locator1 = 'body > table:nth-child(15) > tbody > tr:nth-child(19) > td:nth-child(3)'
    locator_v1 = 'body > table:nth-child(15) > tbody > tr:nth-child(19) > td:nth-child(5)'

    scrap_object = ScrapingHTML(path)
    variable1 = scrap_object.scraping(locator1)
    value1 = scrap_object.scraping(locator_v1)
    print("Variable1: ", variable1)
    print("Value1: ", value1.strip())


if __name__ == "__main__":
    main()
