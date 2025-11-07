import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    time.sleep(3)
    page.goto("https://eztvx.to/home")
    page.locator("input[name=\"q1\"]").click()
    page.locator("input[name=\"q1\"]").fill("Games of Thrones")
    time.sleep(3)
    page.get_by_role("button", name="Search").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
