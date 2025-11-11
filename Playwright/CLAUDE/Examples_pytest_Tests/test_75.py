'''
Example 75: Parametrize Tests (Test with Multiple Data)

New instruction: @pytest.mark.parametrize("param1, param2", [(data1), (data2)])
What it does:

Runs the SAME test multiple times with different data
Each tuple () becomes one test run
username, password, expected_message are the parameters
The test runs 3 times (one for each data set)
Very useful for testing multiple scenarios without repeating code

Expected result: 3 tests run (one for each data combination), all should pass!
'''

import pytest

@pytest.mark.parametrize("username, password, expected_message", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("wronguser", "wrongpass", "Your username is invalid!"),
    ("tomsmith", "wrongpass", "Your password is invalid!"),
])
def test_login_scenarios(page, username, password, expected_message):
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    
    assert expected_message in page.inner_text("body")