from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #page.goto("https://www.google.com")
    page.goto('https://practicesoftwaretesting.com')
    time.sleep(3)
    print("Navigated to Practice Software Testing!")
    print(page.content().istitle())
    browser.close()