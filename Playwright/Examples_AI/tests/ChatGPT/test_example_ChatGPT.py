from playwright.sync_api import sync_playwright

def test_basic_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False opens a visible browser
        page = browser.new_page()
        page.goto("https://playwright.dev")
        print(page.title())  # just to see it works
        browser.close()
