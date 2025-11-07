# import relevant libraries
import requests 
from bs4 import BeautifulSoup
from time import sleep


# define the url
#url = "https://www.feedbooks.com/publicdomain/browse/top?lang=en&page="+str(page_number)
#url = "https://www.feedbooks.com/recent"
#url = "https://market.feedbooks.com/best_sellers"

# path for the offline html file
#path_html = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Scraping_Using_BeautifulSoup\Best Sellers _ Feedbooks.mhtml'

# url for the web page
#url = 'https://market.feedbooks.com/best_sellers'
url = 'https://market.feedbooks.com/recent?page=1'

# send a request to get html code from that url
response = requests.get(url, headers={"Accept": "text/html"}) 
#print(response.text)

# parse the response
parsed_response = BeautifulSoup(response.text, "html.parser")
#print(parsed_response.prettify())

# extract all the elements specific to book titles from that page
title_elements = parsed_response.find_all('a', {
    'class': 'b-details__title',
    'data-post-hog': 'catalog-itemcard-title'
})

# extract all the elements specific to book authors from that page
author_elements = parsed_response.find_all('a', {
    'class': 'link',
    'data-post-hog': 'catalog-itemcard-author'
})

# print out the book titles appearing on that page after formatting the text 
print("\nBook Titles:\n", list(map(lambda x: x.text.strip(), title_elements)))

# print out the book authors appearing on that page after formatting the text 
print("\nBook Authors:\n", list(map(lambda x: x.text.strip(), author_elements)))

# pause the program for 1 second between iterations of the loop
sleep(1)