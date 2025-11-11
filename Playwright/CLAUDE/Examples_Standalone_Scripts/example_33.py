'''
Example 33: Check if Element is Checked
New instruction: is_checked = page.locator("input[type='checkbox']").first.is_checked()
What it does:
•	Finds the first checkbox
•	.is_checked() checks if the checkbox has a checkmark
•	Returns True if checked, False if not checked
Expected result: You should see: First checkbox checked: False (first checkbox is unchecked on this page).

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    is_checked = page.locator("input[type='checkbox']").first.is_checked()
    print(f"First checkbox checked: {is_checked}")
    browser.close()
