'https://www.udemy.com/course/master-web-scraping-with-python/learn/lecture/22143162#overview'

'https://github.com/satssehgal/BookstoreScraper/blob/746495d59da54901aa4bc279c2e6fadfa4597608/bookstoscrape_tutorial.py'
'https://github.com/satssehgal/BookstoreScraper.git'

import requests
import pandas as pd
from bs4 import BeautifulSoup


titles = []
prices = []
stars = []
urlss = []

url = 'http://books.toscrape.com/catalogue/page-1.html'

def scraping(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print(soup.prettify())

    # titles
    for i in soup.findAll('h3'):
        ttl = i.getText()
        titles.append(ttl)

    # prices
    for j in soup.findAll('p', class_ = 'price_color'):
        price = j.getText()
        prices.append(price)

    # stars
    for s in soup.findAll('p', class_ = 'star-rating'):
            for k,v in s.attrs.items():
                star = v[1]
                stars.append(star)

    # urls for books images          
    divs = soup.findAll('div', class_='image_container')
    for thumbs in divs:
        tgs = thumbs.find('img', class_='thumbnail')
        urls = 'http://books.toscrape.com/' + str(tgs['src'])
        newurls = urls.replace("../","")
        urlss.append(newurls)
        
    data={'Titles': titles, 'Prices' : prices, 'Stars' : stars, "URLs" : urlss}
    
    return data



pages_to_scrape = 5

# create a list with the urls for all the pages we want to scrape
pages = []
for i in range(1, pages_to_scrape+1):
    url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
    pages.append(url)

# scrape the number of pages stored in pages_to_scrape
for url in pages:
    data = scraping(url)

df = pd.DataFrame(data=data)
df.index += 1 # to have the index starting with 1
print(df)

df.to_excel(r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Example_Scraping_with_Beautiful_Soup\output.xlsx")