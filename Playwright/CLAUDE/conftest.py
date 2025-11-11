'''
New concept: conftest.py file
What it does:

conftest.py is a special pytest file
Fixtures defined here are available to ALL test files automatically
No need to import them!
Perfect for shared setup code
One conftest.py per folder (tests/, or deeper)

Replace the import with a relative import (.pages, with DOT)

conftest.py vs login_page.py
login_page.py (Page Object):

Contains the page structure (elements, actions)
Reusable class that represents the login page
Used in multiple tests
What: "Here's how to interact with the login page"

conftest.py (Shared Fixtures):

Contains test setup/preparation
Provides ready-to-use instances with @pytest.fixture
Automatically available to all tests
What: "Here's pre-configured stuff tests can use"

Think of it as:
login_page.py = The tool (the class)
conftest.py = The toolbox that hands you the tool ready-to-use
'''

import pytest
from .pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    """Provides a LoginPage instance"""
    return LoginPage(page)

@pytest.fixture
def logged_in_page(page):
    """Provides a page that's already logged in"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    return page