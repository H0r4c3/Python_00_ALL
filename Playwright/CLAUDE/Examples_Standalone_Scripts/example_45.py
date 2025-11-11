'''
Example 45: Get nth Element
New instruction: page.locator("table tr").nth(2)
What it does:
•	Finds all table rows
•	.nth(2) gets the element at index 2 (third element, because counting starts at 0)
•	nth(0) = first, nth(1) = second, nth(2) = third, etc.
•	Gets a specific element by its position
Expected result: You should see the text from the third row.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    third_row = page.locator("table tr").nth(2)
    print(f"Third row text: {third_row.inner_text()}")
    browser.close()
