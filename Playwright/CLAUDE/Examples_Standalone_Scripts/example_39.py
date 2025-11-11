'''
Example 39: Get Element by Alt Text
New instruction: page.get_by_alt_text("User Avatar")
What it does:
•	Finds an image by its alt text (alternative text)
•	Alt text describes what the image shows
•	Useful for finding and interacting with images
Expected result: You should see the mouse hover over the first user image.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.get_by_alt_text("User Avatar").first.hover()
    print("Hovered using alt text!")
    import time
    time.sleep(2)
    browser.close()
