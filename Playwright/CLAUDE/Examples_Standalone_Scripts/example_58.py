'''
Example 58: Take Element Screenshot
New instruction: page.locator("img[alt='Google']").screenshot(path="logo.png")
What it does:
•	Finds a specific element (Google logo)
•	Takes a screenshot of only that element
•	Crops the image to show just that part
•	Useful for capturing specific parts of a page
Expected result: Check your folder - logo.png will contain only the Google logo!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.locator("img[alt='Google']").screenshot(path=r"C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Playwright\logo.png")
    print("Logo screenshot saved!")
    browser.close()
