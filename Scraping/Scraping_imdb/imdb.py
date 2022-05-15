'https://medium.com/@paulau404/python-single-webpage-scraping-tutorial-4f9070be3c83'

import requests
from bs4 import BeautifulSoup
import pandas as pd

# request http
html = requests.get('https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv')
print(html.status_code)

# parse html
soup = BeautifulSoup(html.text, 'html.parser')
movies = soup.find_all('div', attrs={'class': 'lister-item-content'})

# create empty lists for variables needed
titles = []
ratings = []

# loop for crawling
for movie in movies:
    titles.append(movie.find('h3').find('a').text)
    ratings.append(movie.find('div', attrs={'class': 'ratings-bar'}).find('strong').text)
    
# Create DataFrame
movies_df = pd.DataFrame({
    'Title': titles,
    'Rating': ratings
})

# write csv to local disk
path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scraping_imdb\movies.csv'
movies_df.to_csv(path, index=False, encoding='utf-8')