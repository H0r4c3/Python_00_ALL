'''
Example 12: Get Text from Element
New instruction: first_result = page.locator("h3").first.inner_text()
What it does:
•	page.locator("h3") finds all heading elements (search result titles)
•	.first gets only the first one
•	.inner_text() extracts the text from inside that element
•	Stores the text in variable first_result
Expected result: You should see the title of the first Google search result printed in the terminal.

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    first_result = page.locator("h3").first.inner_text()
    print(f"First result: {first_result}")
    browser.close()

