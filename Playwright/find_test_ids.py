from playwright.sync_api import sync_playwright

def find_all_test_ids(url: str):
    """Find all test IDs on a page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        # Find all data-test attributes
        elements = page.locator('[data-test]').all()
        
        print(f"\n=== Test IDs found on {url} ===\n")
        for element in elements:
            test_id = element.get_attribute('data-test')
            tag = element.evaluate('el => el.tagName.toLowerCase()')
            text = element.text_content()[:30] if element.text_content() else ""
            print(f'{tag:15} data-test="{test_id:30}" → {text}')
        
        browser.close()

if __name__ == "__main__":
    find_all_test_ids("https://practicesoftwaretesting.com")