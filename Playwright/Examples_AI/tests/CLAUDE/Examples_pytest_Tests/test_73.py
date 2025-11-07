'''
Example 73: Using Expect Assertions (Better Style)
Playwright has a better way to write assertions.

New instruction: from playwright.sync_api import expect and expect(element).to_contain_text()
What it does:

expect() is Playwright's assertion library
Better error messages than regular assert
Automatically waits for conditions to be true
More readable: expect(page).to_have_url() vs assert "url" in page.url

Expected result: Test passes with better-looking assertions!
'''

from playwright.sync_api import expect

def test_with_expect(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Using expect() instead of assert
    expect(page.locator("h2")).to_contain_text("Login Page")
    expect(page.get_by_label("Username")).to_be_visible()
    
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("body")).to_contain_text("You logged into a secure area!")