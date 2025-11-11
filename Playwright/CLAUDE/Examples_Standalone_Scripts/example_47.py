'''
Example 47: Press Multiple Keys
New instruction: page.press("textarea[name='q']", "Control+A")
What it does:
•	Presses multiple keys at once (keyboard shortcuts)
•	"Control+A" holds Control and presses A (selects all text)
•	Other examples: "Control+C" (copy), "Control+V" (paste)
•	Use + to combine keys
Expected result: You should see all text in the search box get selected (highlighted).

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name='q']", "playwright python")
    page.press("textarea[name='q']", "Control+A")
    print("Selected all text!")
    import time
    time.sleep(2)
    browser.close()
