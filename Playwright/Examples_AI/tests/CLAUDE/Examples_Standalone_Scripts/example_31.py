'''
Example 31: Get Multiple Elements Text
New instruction: results = page.locator("h3").all_inner_texts()
What it does:
•	Finds all h3 elements (all search result titles)
•	.all_inner_texts() gets the text from ALL of them
•	Returns a list of texts ["first result", "second result", ...]
Expected result: You should see a list with all search result titles.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    results = page.locator("h3").all_inner_texts()
    print(f"All results: {results}")
    browser.close()
