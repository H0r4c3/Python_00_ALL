from pathlib import Path
from playwright.sync_api import sync_playwright

def test_homepage_title():
    # Arrange
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # change to False to see the browser
        page = browser.new_page()

        # Act
        page.goto("https://playwright.dev/python/")

        # Assert
        assert "Playwright" in page.title

        # (Optional) save a screenshot to artifacts/
        out = Path("artifacts")
        out.mkdir(exist_ok=True)
        page.screenshot(path=str(out / "homepage.png"))

        browser.close()
