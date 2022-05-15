'https://andrew-muller.medium.com/beautifulsoup-basics-bbb96026e1c0'

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Web_scraping'
content = requests.get(url).text

soup = BeautifulSoup(content, 'html.parser')

# To get the information into Python, use BeautifulSoup’s .find() method. 
# The first argument is the type of html tag (the first word after the ‘<’), and the second is a dictionary of the other elements the tag may contain.
toc = soup.find('div', {'id':'toc', 'class':'toc'})


# Let’s pull all of the section headers out of this table of contents and put them into a list. 
# Taking a look back at the HTML, you might see that each of the headers is in an <li> tag, for ‘list item’. 
# BeautifulSoup is able to grab them all at once with the .find_all() method. 
# This returns a list of every matching tag. 
# To get just the text from those tags, we will have to use the .get_text() method on each of those tags, then store the results in a list.
headers = [header.get_text().split('\n')[0] for header in toc.find_all('li')]
print(headers)


# Full function is here
def get_wiki_headers(title):
    """
    Uses BeautifulSoup and requests to scrape a Wikipedia page via the article title and return a list of strings containing 
    all headers and subheaders in the article.
    """
    url = 'https://en.wikipedia.org/wiki/' + title.replace(' ', '_')
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    toc = soup.find('div', {'id':'toc', 'class':'toc'})
    headers = [header.get_text().split('\n')[0] for header in toc.find_all('li')]
    return headers


#get_wiki_headers(title)
