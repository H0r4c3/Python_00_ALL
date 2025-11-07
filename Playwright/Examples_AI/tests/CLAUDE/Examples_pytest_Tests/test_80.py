'''
Example 80: Conftest.py (Shared Fixtures)

New concept: conftest.py file
What it does:

conftest.py is a special pytest file
Fixtures defined here are available to ALL test files automatically
No need to import them!
Perfect for shared setup code
One conftest.py per folder (tests/, or deeper)

Expected result: Both tests pass using the shared fixtures!
'''

def test_login_with_fixture(login_page):
    # login_page fixture is automatically available!
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    assert login_page.is_login_successful()

def test_already_logged_in(logged_in_page):
    # This test starts already logged in!
    assert "secure" in logged_in_page.url
    
    # Test logout
    logged_in_page.get_by_role("link", name="Logout").click()
    assert "login" in logged_in_page.url