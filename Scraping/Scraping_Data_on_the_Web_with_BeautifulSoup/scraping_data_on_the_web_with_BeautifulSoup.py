'https://hackersandslackers.com/scraping-urls-with-beautifulsoup/'

import requests
from bs4 import BeautifulSoup

# We need to recognize that a lot of sites have precautions to fend off scrapers from accessing their data.
# The first thing we can do to get around this is spoofing the headers we send along with our requests to make our scraper look like a legitimate browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "http://example.com"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

# Passing a positional argument to find_all will return all anchor tags on the site
# Find all <a> tags
print('Find all <a> tags')
print(soup.find_all("a"))

# We can also find all anchor tags which have the class name "boy". Passing the class_ argument allows us to filter by class name. Note the underscore!
# Find all <a> tags assigned a certain class.
print('Find all <a> tags assigned a certain class.')
print(soup.find_all("a", class_="boy"))

# We can search for elements by id in the same way we searched for classes.
# Remember that we should only expect a single element to be returned with an id, so we should use find here:
print('Find element by ID.')
print(soup.find("a", id="link1"))

# Find elements by attribute.
print('Find elements by attribute.')
print(soup.find_all(attrs={"data-args": "bologna"}))

'''
CSS Selectors
Searching HTML using CSS selectors is one of the most powerful ways to find what you're looking for.
Using CSS selectors enables us to find and leverage highly-specific patterns in the target's DOM structure. 
This is the best way to ensure we're grabbing exactly the content we need.
'''

# Find elements via CSS selector syntax.
# In this example, we're looking for an element that has a "widget" class, as well as an "author" class.
# Once we have that element, we go deeper to find any paragraph tags held within that widget.
print('Find elements via CSS selector syntax.')
print(soup.select(".widget.author p"))

# We could also modify this to get only the second paragraph tag inside the author widget
print(soup.select(".widget.author p:nth-of-type(2)"))

# A specific pattern like this is  likely unique to only a single collection of <li> tags on the page we're exploiting.
print(soup.select("body > div:first-of-type > div > ul li"))

# Get elements and extract attribute values.
# The .get method can be used here to retrieve values of attributes on a tag
# Finds the destination URLs for all <a> tags on a page.
print(soup.find('a').get('href'))

# Another example can have us grab a site's logo image:
# Get <img> element's source link
print(soup.find(id="logo").get('src'))

# Sometimes it's not attributes we're looking for, but just the text within a tag:
# Get elements and extract text content.
print(soup.find('p').get_text())


'''
Pesky Tags to Deal With
n our example of creating link previews, a good first source of information would obviously be the page's meta tags: specifically the og tags they've specified to openly provide the bite-sized information we're looking for. 
Grabbing these tags are a bit more difficult to deal with.
Meta tags are an especially interesting case; they're all uselessly dubbed 'meta', thus we need a second identifier (in addition to the tag name) to specify which meta tag we care about. 
Only then can we bother to get the actual content of said tag.
'''

# Scrape metatags
print(soup.find("meta", property="og:description").get('content'))

'''
If we were to try the above selector on an HTML page that did not contain an og:description, our script would break unforgivingly. 
Not only do we miss this data, but we miss out on everything entirely - this means we always need to build in a plan B, 
and at the very least deal with a lack of tag altogether.
'''
