'https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

webdriver_path_64 = r'C:/Users/Horace.000/AppData/Local/Programs/Python/Python310/EdgeDriverServer/msedgedriver_win64.exe'
webdriver_path_32 = r'C:/Users/Horace.000/AppData/Local/Programs/Python/Python310/EdgeDriverServer/msedgedriver_win32.exe'

# If you are testing on your local machine, this opens an instance of Edge, locally. 
# This command lets you perform tests on it until you use the .close() method to end the connection to the browser.
driver = webdriver.Edge(webdriver_path_64)

# Next, use the .get() method of the driver to load a website. 
# You may also load a local development site as this process is equivalent to opening a window of Chrome on your local machine, typing a URL and hitting Enter. 
# The .get() method not only starts loading a website, but also waits for it to render completely before moving on to the next step.
driver.get("https://www.python.org")

# Once the page loads successfully, you can use the .title attribute to access the textual title of the webpage. 
print(driver.title)

# Next, let us submit a query in the search bar. 
# First, select the element from the HTML DOM and enter a value into it and submit the form by emulating the Return key press. 
# You can select the element using its CSS class, ID, its name attribute, or even the tag name. 
# If you check the source of the query search bar, you notice that the name attribute of this DOM element is “q”.
#search_bar = driver.find_element_by_name("q")
search_bar = driver.find_element(By.NAME, "q")

# Once the DOM element is selected, you first need to clear its contents using the .clear() method, 
# enter a string as its value using the .send_keys() method and finally, emulate the press of the Return key using Keys.RETURN.
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# You notice in the window that these actions trigger a change in the URL with the search results in the window. 
# To confirm the current URL of the window, you can use the following command.
print(driver.current_url)

# To close the current session, use the .close() method. It also disconnects the link with the browser.
driver.close()

'''
In the example, we selected the search bar and queried for a string. Let us explore the selection further. 
Here is the HTML of the search bar:
<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

In the example, we used the .find_element_by_name() method, which searches for the attribute name within the input HTML tag. We can also search for this term using other methods.

CSS ID: .find_element_by_id(“id-search-field”)
DOM Path: .find_element_by_xpath(“//input[@id=’id-search-field’]”)
CSS class: .find_element_by_class_name(“search-field”)
While the CSS ID is unique to every element by design, you may find multiple results when searching through the class name. 
Further, when you search through the DOM path of the element, you can be certain of what you are searching for.
'''