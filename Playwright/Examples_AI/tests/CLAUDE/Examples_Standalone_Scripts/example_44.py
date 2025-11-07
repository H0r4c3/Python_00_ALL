'''
Example 44: Get All Locators
New instruction: rows = page.locator("table tr").all()
What it does:
•	Finds all table rows
•	.all() returns a list of all matching elements (not just one)
•	You can then loop through them with for
•	[:3] means take only first 3 rows
Expected result: You should see the text from the first 3 rows printed.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/tables")
    rows = page.locator("table tr").all()
    print(f"Number of rows: {len(rows)}")
    for row in rows[:3]:
        print(row.inner_text())
    browser.close()
