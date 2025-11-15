'''
Example 13: Count Elements
New instruction: count = page.locator("h3").count()
What it does:
•	Finds all h3 elements (result titles)
•	.count() counts how many elements were found
•	Returns a number
Expected result: You should see something like: Number of results found: 10

'''

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.fill('[data-test=\"search-query\"]', "hammer")
    time.sleep(3)
    page.press('[data-test=\"search-submit\"]', "Enter")
    page.wait_for_load_state("networkidle")
    time.sleep(3)
    count = page.locator("a.card").count() # card is from class="card"
    print(f"Number of results found: {count}")
    browser.close()

