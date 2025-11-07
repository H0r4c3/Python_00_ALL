'''
Example 63: Drag and Drop
New instruction: page.drag_and_drop("#column-a", "#column-b")
What it does:
•	Drags element from first selector to second selector
•	"#column-a" the element to drag (source)
•	"#column-b" where to drop it (target)
•	Like clicking, holding, dragging, and releasing with mouse
Expected result: You should see column A and column B swap positions!

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    page.drag_and_drop("#column-a", "#column-b")
    print("Dragged and dropped!")
    import time
    time.sleep(2)
    browser.close()
