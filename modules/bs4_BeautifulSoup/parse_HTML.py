'https://medium.com/python-in-plain-english/10-automation-scripts-for-your-daily-python-projects-892a82be3f75'

from bs4 import BeautifulSoup
html = """ 
<html>
    <head> 
        <title> 
            My Page 
        </title> 
    </head> 
    <body> 
        <div class="city">
            <p> My first paragraph. </p> <p> My second paragraph. </p> 
        </div>
    </body> 
 </html> """
soup = BeautifulSoup(html, 'html.parser')
# Prettify the HTML
print(soup.prettify())
# Find Single data
data = soup.find('p').text
# Find all data
data = soup.find_all('p')
# Find by artibute
data = soup.find_all(class_='city')
# Find by tag and attributes
data = soup.find("div", attrs={"class": "city"}).text
# Get title tag
print(data.title.text)
# Get all text
print(data.text)