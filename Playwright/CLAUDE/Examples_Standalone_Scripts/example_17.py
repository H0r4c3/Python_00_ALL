'''
Example 17: Select from Dropdown
New instruction: page.select_option("select#dropdown", "1")
What it does:
•	Finds a dropdown menu using selector "select#dropdown"
•	Selects the option with value "1"
•	Like clicking a dropdown and choosing an option
Expected result: You should see the dropdown change to "Option 1".

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("select#dropdown", "1")
    print("Option 1 selected!")
    import time
    time.sleep(2)
    browser.close()
