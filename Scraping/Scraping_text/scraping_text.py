# Scraping only the text from a website

import requests
from bs4 import BeautifulSoup

path1 = 'https://www.delicateseliterare.ro/lista-carti-lee-child/'
locator1 = 'div.post-content'

path2 = 'https://literaturapetocuri.ro/lista-carti-scrise-de-lee-child.html'
locator2 = 'div.span8.column_container.td-post-content'

page_content = requests.get(path1).content
soup = BeautifulSoup(page_content, 'html.parser')
all_text_string = soup.select_one(locator1).text

list_of_words = all_text_string.split() # eliminate the multiple spaces and creates a list of words
string_of_words = ' '.join(list_of_words) # creates a string from all the words, having a space between them

print(string_of_words)