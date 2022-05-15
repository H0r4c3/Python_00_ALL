'''
https://careerkarma.com/discussions/projects/beginners-web-scraping-447/
A very basic script to scrape course information from all pages of Class Central's data science pages.
'''

# ClassCentral Data Science Course Scraping
# Austin Caudill
# Last Update: 6/04/2021

import requests
from bs4 import BeautifulSoup


def getData(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    datas = soup.findAll('a', href=True, attrs={
                         'class': 'color-charcoal small-down-text-2 text-3', 'data-track-click': 'listing_click'}, text=True)
    for dataIndex in range(len(datas)):
        data = eval(datas[dataIndex]['data-track-props'])['clickMetadata']
        yield [data['courseId'], data['course'], data['institutionId'], data['institution'], data['providerId'], data['provider']]


f = 0
n = 1
while True:
    data = list(
        getData(f'https://www.classcentral.com/subject/data-science?page={f}'))
    f = f+1
    if data == []:
        break
    for x in data:
        print(f'Entry No:     {n}')
        print(f'Course:       {x[0]} - {x[1]}')
        print(f'Institution:  {x[2]} - {x[3]}')
        print(f'Provider:     {x[4]} - {x[5]}')
        print('\n\n')
        print('*'*80)
        print('\n\n')
        n += 1
