'https://docs.google.com/presentation/d/1Ey-BrTONJb6h7lAS2s08Hq5ZnRfD4LI2M3NoQVAbrW8/edit#slide=id.g3fa8a85a47_0_370'

'https://github.com/antoniablair/pyladies_scraping_workshop/blob/master/imdb_exercise_1_solution.md'


import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/title/tt0451279/')
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.h1.get_text()
summary = soup.find('div', class_='summary_text').get_text()
rating = soup.find('span', itemprop='ratingValue').get_text()

print('Title: {}'.format(title)) # if using python 2, just print 'Title {}'.format(title) will work
print('Summary: {}'.format(summary))
print('Rating: {}'.format(rating))