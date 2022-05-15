'https://www.udemy.com/course/python-programming-beginner-to-advanced/learn/lecture/17944178#overview'

import requests
from bs4 import BeautifulSoup


url_emag = 'https://www.emag.ro/search/telefoane-mobile/m62/c?ref=list'
url2 = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi'
#path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\BeautifulSoup\emag_html.py'
#path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\BeautifulSoup\emag.html'

response = requests.get(url_emag) # -> 200, if the page is found

page_content = response.content

#print(response)
#print(response.status_code)

soup = BeautifulSoup(page_content, 'html.parser')
# print(soup.prettify())

# emag
def emag():
    cards = soup.find_all("div", attrs={"class" : "card-item card-standard js-product-data"})

    for card in cards:
        title = card.find("a", attrs={"data-zone" : "title"})
        price = card.find("p", attrs={"class" : "product-new-price"})
        colors = card.find("a", attrs={"class" : "btn btn-xs btn-alt gtm_139rp27 js-product-url"})
    
        print(f'Title: {title.text}, Price: {price.text[:-6] + price.text[-4:]}, Colors: {colors.text}')

    
emag()


# magicbricks
def magicbricks():
    '''
    Scraping ALL the cards on a page
    '''
    cards = soup.find_all("div", attrs={"class" : "flex relative clearfix m-srp-card__container"})

    for card in cards:
        price = card.find("div", attrs={"class" : "m-srp-card__price"})
        title = card.find("span", attrs={"class" : "m-srp-card__title__bhk"})
        title = title.text.strip("\n")
        carpet_area = card.find("div", attrs={"class" : "m-srp-card__summary__info"})
        print(f'Title: {title}, Area: {carpet_area.text}, Price: {price.text}')
        
#magicbricks()




def magicbricks_1():
    '''
    Scraping only 1 card
    '''
    card = soup.find("div", attrs={"class" : "flex relative clearfix m-srp-card__container"})

    price = card.find("div", attrs={"class" : "m-srp-card__price"})
    title = card.find("span", attrs={"class" : "m-srp-card__title__bhk"})
    title = title.text.strip("\n")
    carpet_area = card.find("div", attrs={"class" : "m-srp-card__summary__info"})
    print(f'Title: {title}, Area: {carpet_area.text}, Price: {price.text}')

#magicbricks_1()

