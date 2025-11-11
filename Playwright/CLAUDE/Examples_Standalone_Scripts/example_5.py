'''
Example 5: Wait Before Closing
New instruction: time.sleep(3)
What it does:
•	Pauses the program for 3 seconds
•	This lets you SEE the page before it closes
•	The number is in seconds (you can use 5, 10, etc.)
•	Also new: import time at the top - needed to use time.sleep()
Expected result: Now the browser stays open for 3 seconds 
so you can see Google, then closes.
'''

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    time.sleep(3)
    browser.close()

