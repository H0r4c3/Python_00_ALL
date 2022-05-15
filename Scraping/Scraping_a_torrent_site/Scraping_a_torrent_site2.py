'''
Created on Dec 25, 2020

@author: Horace.000
'''
import requests

from bs4 import BeautifulSoup


Movie = 'your-honor'
path = 'https://eztv.re/search/' + Movie
page_content = requests.get(path).content

soup = BeautifulSoup(page_content, 'html.parser')

locator = 'tr.forum_header_border td.forum_thread_post a.magnet'
lines = soup.select(locator)

print("Line:", lines[0])
print("Dict:", lines[0].attrs)
print('Title:', lines[0].attrs['title'])

print("TORRENTS:")

for item in lines:
    print(item.attrs['title'])
    # print(item.attrs)

print(len(lines))


