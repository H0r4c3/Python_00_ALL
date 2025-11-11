'''
Example 3: Open a Page (Tab)
New instructions: 
context = browser.new_context()
page = context.new_page()
What it does:
When you call browser.new_page(), Playwright automatically creates a default context for you. 
When you call context = browser.new_context() and page = context.new_page(), you explicitly create the context yourself, giving you more control.
•	Opens a new tab/page in the browser
•	Like clicking "New Tab" manually
•	Stores the page in variable page so you can use it
Expected result: Chrome opens with a blank tab, then closes.

For example, context would be useful in this situation:
Testing multiple user sessions:
def test_multiple_users(browser):
    # Admin context
    admin_context = browser.new_context(storage_state='admin_auth.json')
    admin_page = admin_context.new_page()
    
    # Regular user context
    user_context = browser.new_context(storage_state='user_auth.json')
    user_page = user_context.new_page()
    
    # Test interaction between two users
    admin_page.goto('/admin/users')
    user_page.goto('/profile')
'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    print("New page opened!")
    
    context.close()
    browser.close()
