'''
Example 74: Test Fixtures (Setup and Teardown)

New instruction: @pytest.fixture and def login_page(page):
What it does:

@pytest.fixture creates reusable setup code
login_page fixture runs before each test that uses it
Both tests get a fresh page already at the login URL
Reduces code duplication - you don't repeat page.goto() in every test

Expected result: Both tests pass, each starting at the login page automatically!
'''

import pytest

@pytest.fixture
def login_page(page):
    # Setup: Navigate to login page
    page.goto("https://the-internet.herokuapp.com/login")
    return page

def test_login_success(login_page):
    # Test uses the fixture
    login_page.get_by_label("Username").fill("tomsmith")
    login_page.get_by_label("Password").fill("SuperSecretPassword!")
    login_page.get_by_role("button", name="Login").click()
    
    assert "secure" in login_page.url

def test_login_failure(login_page):
    # Another test using the same fixture
    login_page.get_by_label("Username").fill("wronguser")
    login_page.get_by_label("Password").fill("wrongpass")
    login_page.get_by_role("button", name="Login").click()
    
    assert "Your username is invalid!" in login_page.inner_text("body")