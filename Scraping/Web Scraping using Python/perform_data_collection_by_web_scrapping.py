'https://sujaypatel6010.medium.com/web-scraping-using-python-25db6a14d664    (use Private Session in Edge for opening the link)'

import requests
from bs4 import BeautifulSoup
import pandas as pd

# open the URL and extract the data from the website
url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

req = requests.get(url)

# Create empty lists, we will use them, in future, for storing data of specific column.
nm = []
pr = []
rt = []

# Using the Find and Find All methods in BeautifulSoup, we extract the data and store it in the variable.
content = BeautifulSoup(req.content, 'html.parser')

#print(content)

name = content.find_all('div', {"class":"_4rR01T"})
price = content.find_all('div', {"class":"_30jeq3 _1_WHN1"})
rating = content.find_all('div', {"class":"_3LWZIK"})

# Using append, we store the details in the Array that we have created before
for item in name:
    nm.append(item.text)
for item in price:
    pr.append(item.text)
for item in rating:
    rt.append(item.text)
    
# Store the data to a “Comma Separated Values(.csv)” file using the following code. 
# In this lines it is coded that in .csv file there will be three column name “ NAME”, “PRICE”, “RATING” and 
# every data will be under this column accordingly. 
# We have used Pandas for data manipulation.

#data = {'NAME' : nm, 'PRICE' : pr, 'RATING' : rt}
data = {'NAME' : nm, 'PRICE' : pr}
df = pd.DataFrame(data)

path = r'C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Scraping\Web Scraping using Python\my_data.csv'
df.to_csv(path)

