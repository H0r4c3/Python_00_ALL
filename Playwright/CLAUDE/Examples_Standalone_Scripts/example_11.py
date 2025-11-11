'''
Example 11: Wait for Navigation
New instruction: page.wait_for_load_state("networkidle")
What it does:
•	Waits until the page finishes loading completely
•	"networkidle" means wait until network activity stops (no more loading)
•	Ensures the page is ready before taking next action
Expected result: Now, it waits for search results to fully load before printing the message.

'''
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicesoftwaretesting.com")
    page.fill('[data-test=\"search-query\"]', "hammer")
    time.sleep(5)
    page.press('[data-test=\"search-query\"]', "Enter")
    page.wait_for_load_state("networkidle")
    print("Page fully loaded!")
    time.sleep(2)
    browser.close()