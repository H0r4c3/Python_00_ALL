'''
Created on Dec 25, 2020

@author: Horace.000
'''
import requests
import pandas as pd

from bs4 import BeautifulSoup

from HTML_code_for_eztv_site_for_Scraping import page_content    # page_content = requests.get('https://eztv.re/shows/23839/his-dark-materials/').content


soup = BeautifulSoup(page_content, 'html.parser')

line_hover = soup.select('tr.forum_header_border td.forum_thread_post a.magnet')

df = pd.DataFrame(line_hover)


print(line_hover[0])
print(line_hover[0].attrs)
print(line_hover[0].attrs['title'])


print("TORRENTS:")

for item in line_hover:
    print(item.attrs['title'])
    # print(item.attrs)

print(len(line_hover))
