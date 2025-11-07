'''
New concepts:

Multiple assert statements in one test
Test passes only if ALL assertions pass
If any assertion fails, the test stops and fails

You should see the test pass with all assertions working!
'''

def test_login_page_assertions(page):
    # Using a demo website that works reliably
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Multiple assertions
    assert "Login Page" in page.inner_text("h2")
    assert page.get_by_label("Username").is_visible()
    assert page.get_by_label("Password").is_visible()
    
    # Fill the form
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    
    # Click login
    page.get_by_role("button", name="Login").click()
    
    # Assert successful login
    page.wait_for_url("**/secure")
    assert "secure" in page.url
    assert "You logged into a secure area!" in page.inner_text("body")