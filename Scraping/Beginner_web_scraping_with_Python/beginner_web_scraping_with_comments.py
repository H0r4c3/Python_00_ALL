'https://www.codementor.io/@garethdwyer/beginner-web-scraping-with-python-and-repl-it-nzr27jvnq'


import requests
import string # To identify all the capital letters in our alphabet

from collections import Counter # To find the most common nouns in a list, once we have built a list of all the nouns.

from bs4 import BeautifulSoup

url = "https://bbc.com/news"

page_content = requests.get(url).content
soup = BeautifulSoup(page_content, "html.parser")

links = soup.select("a") # find all the 'a' elements in our HTML and extract them to a list. 

# The <a> element in HTML was used to define links, with the 'href' attribute being used to specify where the link should go to

news_urls = []
for link in links:
    href = link.get("href")
    if href.startswith("/news") and href[-1].isdigit():
        news_url = "https://bbc.com" + href
        news_urls.append(news_url)



'''
We can fetch the data for each one of these individual articles. 
As a toy project, let's extract the proper nouns (people, places, etc) from each article and print out the most common ones
'''
all_nouns = []
for url in news_urls[:10]:
    print("Fetching {}".format(url))
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    words = soup.text.split() # splits (on white space) this resulting big body of text into individual words

    # The next line loops through all the words in that given article and keeps only the ones that are made up of numeric characters and which start with a capital letter
    nouns = [word for word in words if word.isalpha() and word[0] in string.ascii_uppercase]
    all_nouns += nouns

# We print out the 100 most common nouns along with a count of how often they appeared in all 10 of the articles we looked at
print(Counter(all_nouns).most_common(100))