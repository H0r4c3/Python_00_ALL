'''
Example 41: Get Element by Test ID
New instruction: page.get_by_test_id("search-button")
What it does:
•	Finds an element by its test ID attribute (usually data-testid)
•	Test IDs are special attributes developers add specifically for testing
•	Most reliable way to find elements in professional testing
•	Note: This example might not work on Google since they don't use test IDs
Expected result: This might fail on Google, but you learned the instruction!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.get_by_test_id("search-button").click()
    print("Clicked using test ID!")
    import time
    time.sleep(2)
    browser.close()
