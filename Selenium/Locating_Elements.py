'https://selenium-python.readthedocs.io/locating-elements.html'

'''
There are various strategies to locate elements in a page. You can use the most appropriate one for your case. 
Selenium provides the following methods to locate elements in a page:

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector


To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector


Apart from the public methods given above, there are two private methods which might be useful for locating page elements:

find_element
find_elements
Example usage:
'''

from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')


#These are the attributes available for By class:

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

# Locating by Id
'''
Use this when you know the id attribute of an element. With this strategy, the first element with a matching id attribute will be returned. 
If no element has a matching id attribute, a NoSuchElementException will be raised.

For instance, consider this page source:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
</html>

The form element can be located like this:
'''
login_form = driver.find_element_by_id('loginForm')


# Locating by Name

'''
Use this when you know the name attribute of an element. With this strategy, the first element with a matching name attribute will be returned. 
If no element has a matching name attribute, a NoSuchElementException will be raised.

For instance, consider this page source:
'''
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

'''
This will give the “Login” button as it occurs before the “Clear” button:
continue = driver.find_element_by_name('continue')
'''


# Locating by XPath

'''
XPath is the language used for locating nodes in an XML document.
HTML can be an implementation of XML (XHTML)
One of the main reasons for using XPath is when you don’t have a suitable id or name attribute for the element you wish to locate.

The form elements can be located like this:
'''
login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")

'The username element can be located like this:'
username = driver.find_element_by_xpath("//form[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")
'''
First form element with an input child element with name set to username
First input child element of the form element with attribute id set to loginForm
First input element with attribute name set to username
'''

'The “Clear” button element can be located like this:'
clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
'''Input with attribute name set to continue and attribute type set to button
Fourth input child element of the form element with attribute id set to loginForm
'''

# Locating Hyperlinks by Link Text
'''
Use this when you know the link text used within an anchor tag. With this strategy, the first element with the link text matching the provided value will be returned. If no element has a matching link text attribute, a NoSuchElementException will be raised.

For instance, consider this page source:

<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
</html>
The continue.html link can be located like this:
'''
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')


# Locating Elements by Tag Name
'''
Use this when you want to locate an element by tag name. With this strategy, the first element with the given tag name will be returned. If no element has a matching tag name, a NoSuchElementException will be raised.

For instance, consider this page source:

<html>
 <body>
  <h1>Welcome</h1>
  <p>Site content goes here.</p>
</body>
</html>
The heading (h1) element can be located like this:
'''
heading1 = driver.find_element_by_tag_name('h1')


# Locating Elements by Class Name
'''
Use this when you want to locate an element by class name. With this strategy, the first element with the matching class name attribute will be returned. If no element has a matching class name attribute, a NoSuchElementException will be raised.

For instance, consider this page source:

<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
</html>
The “p” element can be located like this:
'''
content = driver.find_element_by_class_name('content')


# Locating Elements by CSS Selectors
'''
Use this when you want to locate an element using CSS selector syntax. With this strategy, the first element matching the given CSS selector will be returned. If no element matches the provided CSS selector, a NoSuchElementException will be raised.

For instance, consider this page source:

<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
</html>
The “p” element can be located like this:
'''
content = driver.find_element_by_css_selector('p.content')

