import pytest
from utils.data_reader import load_users
from pages.login_page import LoginPage

users = load_users()


@pytest.mark.regression
@pytest.mark.parametrize("user", users)
def test_login_data_driven(page, config, user):
    login_page = LoginPage(page)
    base_url = config["base_url"]

    login_page.open(base_url)
    login_page.login(user["email"], user["password"])

    if user.get("valid"):
        login_page.assert_logged_in()
    else:
        login_page.assert_login_error()
