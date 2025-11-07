'''
Example 6: Get Page Title
New instruction: title = page.title()
What it does:
•	Gets the title of the webpage
•	The title is what you see in the browser tab at the top
•	Stores it in variable title so we can print it
Expected result: You see in the terminal something like: Page title is: Google

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #page.goto("https://www.google.com")
    page.goto('https://practicesoftwaretesting.com')
    #page.goto('https://h0r4c3.github.io/checkyourmole-site')
    title = page.title()
    print(f"Page title is: {title}")
    browser.close()

