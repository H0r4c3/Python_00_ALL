'''
Created on Dec 25, 2020

@author: Horace.000
'''
import requests
import pandas as pd

from bs4 import BeautifulSoup

from HTML_code_for_eztv_site_for_Scraping import page_content    # page_content = requests.get('https://eztv.re/shows/23839/his-dark-materials/').content


soup = BeautifulSoup(page_content, 'html.parser')

line_hover = soup.select('tr.forum_header_border')

line_hover_magnet = soup.select('tr.forum_header_border td.forum_thread_post a.magnet')
line_hover_zoink = soup.select('tr.forum_header_border td.forum_thread_post a.download_1')
line_hover_seeds = soup.select('tr.forum_header_border td.forum_thread_post')

line_hover_forum_thread_post = soup.select('tr.forum_header_border td.forum_thread_post')


Title = []
Magnet = []
Zoink = []
Size = []
Released = []
Seeds = []

for item in line_hover_magnet:
    Title.append(item.attrs['title'])
    Magnet.append(item.attrs['href'])

# Title = [item.attrs['title'] for item in line_hover_magnet]

for item in line_hover_zoink:
    if item != None:
            Zoink.append(item.attrs['href'])
    else:
            Size.append(None)
    

length_size = len(line_hover_forum_thread_post)
length_seeds = len(line_hover_seeds)


for i in range(3, length_size, 6):
    for item in line_hover_forum_thread_post[i]:
        if item != None:
            Size.append(item)
        else:
            Size.append(None)




for i in range(3, length_size, 6):
    if '<td align="center" class="forum_thread_post"></td>' in line_hover_forum_thread_post:
        Size.append(None)
    else:
        Size.append(line_hover_forum_thread_post[i])



for i in range(4, length_size, 6):
    for item in line_hover_forum_thread_post[i]:
        Released.append(item)

for i in range(5, length_seeds, 6):
    for item in line_hover_seeds[i]:
        if item != None:
            Seeds.append(item)
        else:
            Seeds.append(None)

print(len(Title))
print(len(Magnet))
print(len(Zoink))
print(len(Size))
print(len(Released))
print(len(Seeds))

#df = pd.DataFrame({"Title" : Title, "Magnet" : Magnet, "Zoink" : Zoink, "Size" : Size, "Released" : Released}, "Seeds" : Seeds})
df = pd.DataFrame({"Title" : Title, "Magnet" : Magnet, "Released" : Released, "Seeds" : Seeds})
#df = pd.DataFrame({"Size" : Size})



# Converting to excel 
df.to_excel('c:/Users/Horace.000/eclipse-workspace/Python_Project_6_Online_Courses/Misc/Scraping_a_torrent_site/eztv_torrents.xlsx', index = False)

'''
print(line_hover[0])
print(line_hover[0].attrs)
print(line_hover[0].attrs['title'])


print("TORRENTS:")

for item in line_hover:
    print(item.attrs['title'])
    # print(item.attrs)

print(len(line_hover))
'''