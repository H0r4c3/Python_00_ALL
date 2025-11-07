'''
Example 42: Filter Locators
New instruction: page.locator("h3").filter(has_text="Playwright")
What it does:
•	First finds all h3 elements
•	.filter(has_text="Playwright") keeps only those containing the word "Playwright"
•	Useful when you need to narrow down results
•	Then .count() counts how many matched
Expected result: You should see how many results contain "Playwright" in their title.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "Playwright Python")
    page.press("textarea[name='q']", "Enter")
    page.wait_for_load_state("networkidle")
    results = page.locator("h3").filter(has_text="Playwright")
    print(f"Filtered results count: {results.count()}")
    browser.close()
