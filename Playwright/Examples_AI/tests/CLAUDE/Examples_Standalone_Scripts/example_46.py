'''
Example 46: Get Last Element
New instruction: page.locator("table tr").last
What it does:
•	Finds all table rows
•	.last gets the last element in the list
•	Similar to .first but from the end
•	Note: no parentheses () - it's a property, not a method
Expected result: You should see the text from the last row.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    last_row = page.locator("table tr").last
    print(f"Last row text: {last_row.inner_text()}")
    browser.close()
