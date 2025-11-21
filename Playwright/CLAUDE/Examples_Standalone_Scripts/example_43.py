'''
Example 43: Chain Locators
New instruction: page.locator("table").locator("tr").first.locator("td").first
What it does:
•	Chains multiple .locator() calls together
•	First finds the table, then rows inside it, then cells inside the first row
•	.first gets the first match at each step
•	Useful for navigating complex HTML structures
Expected result: You should see the text from the first cell of the first row.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    cell = page.locator("table").locator("tr").first.locator("td").first
    
    #text = cell.inner_text()
    #print(f"First cell text: {text}")
    
    try:
        text = cell.inner_text()
        print(f"First cell text: {text}")
    except Exception as e:
        print(f"Could not retrieve cell text: {e}")
        browser.close()
