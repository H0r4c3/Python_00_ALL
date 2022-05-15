'https://pyshark.com/extract-links-from-a-web-page-using-python/'

import httplib2
import requests
from bs4 import BeautifulSoup, SoupStrainer

class Extractor():
    
    def get_links(self, url):

        http = httplib2.Http()
        response, content = http.request(url)

        links=[]

        for link in BeautifulSoup(content).find_all('a', href=True):
            links.append(link['href'])
        
        return links
    
    def get_links_H(self, url):
        
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'html.parser')
        
        links=[]
        
        for link in soup.find_all('a', href=True):
            links.append(link['href'])
        
        return links
        
        


url = 'https://pyshark.com/'

myextractor = Extractor()

#links = myextractor.get_links(url)

links = myextractor.get_links_H(url)

for link in links:
    print(link)

