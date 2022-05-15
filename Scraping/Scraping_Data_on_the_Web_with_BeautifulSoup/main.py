"""Application entry point."""
import sys

sys.path.append(r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scraping_Data_on_the_Web_with_BeautifulSoup')

from scraper import scrape_page_metadata
from config import URL

#scrape = scrape_page_metadata()

if __name__ == '__main__':
    scrape_page_metadata(URL)
    #scrape_page_metadata('https://example.com/')
