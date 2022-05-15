'https://lms.simplilearn.com/courses/2772/Data-Science-with-Python/syllabus'

from bs4 import BeautifulSoup

# create an html document
html_doc = '''<html>
<body>
<h1>My First Heading</h1>
<b><!--This is a comment line--></b>
<p title="About Me" class="test">My first paragraph.</p>
<div class="cities">
<h2>London</h2>
</div>
</body>
</html>'''

# parse it using html parser
soup = BeautifulSoup(html_doc, 'html.parser')

# view the soup type
print(type(soup))

# view the soup object
print(soup)

# create a tag object
tag = soup.p

# view the tag object type
print(type(tag))

# print the tag
print(tag)

# create a comment object type
comment = soup.b.string

# print the comment
print(comment)

# view tag attributes
print(tag.attrs)

# view tag values
print(tag.string)



