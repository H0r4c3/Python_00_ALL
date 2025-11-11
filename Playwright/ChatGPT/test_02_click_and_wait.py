from playwright.sync_api import sync_playwright

def test_open_docs_from_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")

        # Click the "Docs" link in the top nav (role-based selector is robust)
        page.get_by_role("link", name="Docs").click()

        # Wait until URL contains /python/docs
        page.wait_for_url("**/python/docs/**")

        assert "Docs" in page.title()
        browser.close()
