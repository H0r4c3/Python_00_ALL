'''
Example 20: Hover Over Element
New instruction: page.hover("div.figure")
What it does:
•	Finds an element using selector "div.figure"
•	.hover() moves the mouse over that element
•	Like moving your mouse over something without clicking
Expected result: You should see text appear when hovering over the first image.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.hover("div.figure")
    print("Hovered over image!")
    import time
    time.sleep(2)
    browser.close()
