'''
Example 27: Get All Text from Page
New instruction: all_text = page.inner_text("body")
What it does:
•	"body" selects the entire page body (all visible content)
•	.inner_text() extracts all the text from it
•	Returns all visible text on the page as one string
Expected result: You should see all the text from Google's homepage printed in the terminal.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    all_text = page.inner_text("body")
    print(f"Page text: {all_text}")
    browser.close()
