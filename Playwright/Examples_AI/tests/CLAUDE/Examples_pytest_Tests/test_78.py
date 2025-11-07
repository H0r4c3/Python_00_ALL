'''
Example 78: Page Object Model (POM) - Part 1
This is a design pattern that companies love! Let's organize code better.
Create folder structure:
tests/
├── pages/
│   └── login_page.py
└── test_pom.py

New concept: Page Object Model (POM)
What it does:

Separates page elements and actions into a class
Test code is cleaner and more readable
If page changes, you only update one file (login_page.py)
Reusable across multiple tests
This is what companies want to see!

Expected result: Test passes using the LoginPage class!
'''

import sys
from pathlib import Path

# Add the tests folder to Python path
tests_folder = Path(__file__).parent.parent.parent
sys.path.insert(0, str(tests_folder))

from pages.login_page_OLD import LoginPage

def test_login_with_pom(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    assert "secure" in page.url

