'''
Example 77: Test Markers (Organize Tests)

New instruction: @pytest.mark.smoke and @pytest.mark.e2e (using markers from your pytest.ini)
What it does:

Organizes tests into categories (smoke, e2e)
You can run only specific markers
smoke = quick tests, e2e = full end-to-end tests
Useful in CI/CD pipelines

Expected result: All 4 tests pass!

Run different ways:
All tests:
bashpytest tests/test_markers.py -v
Only smoke tests (fast):
bashpytest tests/test_markers.py -v -m smoke
Only e2e tests (slow):
bashpytest tests/test_markers.py -v -m e2e
'''

import pytest

@pytest.mark.smoke
def test_homepage_loads(page):
    page.goto("https://the-internet.herokuapp.com")
    assert "The Internet" in page.inner_text("h1")

@pytest.mark.smoke
def test_login_page_loads(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.inner_text("h2")

@pytest.mark.e2e
def test_full_login_flow(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    assert "secure" in page.url

@pytest.mark.e2e
def test_logout_flow(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Logout").click()
    assert "login" in page.url