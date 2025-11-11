'''
Example 48: Type Text Slowly
New instruction: page.type("textarea[name='q']", "Playwright", delay=200)
What it does:
•	Types text character by character (like a human typing)
•	delay=200 waits 200 milliseconds between each character
•	.fill() is instant, .type() is slow and visible
•	Good for testing or demonstrations
Expected result: You should see "Playwright" typed letter by letter slowly.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.type("textarea[name='q']", "Playwright", delay=200)
    print("Typed slowly!")
    import time
    time.sleep(2)
    browser.close()
