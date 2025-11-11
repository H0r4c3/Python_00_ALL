'''
Example 62: Get Bounding Box (Element Position)
New instruction: box = page.locator("img[alt='Google']").bounding_box()
What it does:
•	Gets the position and size of an element
•	Returns a dictionary with: x, y (position), width, height (size)
•	x, y are pixels from top-left corner of page
•	Useful for checking element placement
Expected result: You should see the Google logo's position and size in pixels.

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    box = page.locator("img[alt='Google']").bounding_box()
    print(f"Logo position: x={box['x']}, y={box['y']}, width={box['width']}, height={box['height']}")
    browser.close()
