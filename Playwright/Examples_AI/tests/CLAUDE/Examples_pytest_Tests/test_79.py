'''
Example 79: Page Object Model (POM) - Part 2 (With Assertions)

Let's improve the LoginPage with assertion methods!

New concept: Methods in Page Object for assertions
What it does:

is_login_successful() checks if login worked
get_error_message() retrieves error text
Tests are even cleaner - all logic in the page object
Very professional approach

Expected result: Both tests pass!
'''

import sys
from pathlib import Path

# Add the tests folder to Python path
tests_folder = Path(__file__).parent.parent.parent
sys.path.insert(0, str(tests_folder))

from pages.login_page import LoginPage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    assert login_page.is_login_successful()
    assert "secure" in page.url

def test_failed_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wronguser", "wrongpass")
    
    assert "Your username is invalid!" in login_page.get_error_message()