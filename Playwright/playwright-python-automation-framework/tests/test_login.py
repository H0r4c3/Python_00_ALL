import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_success(page, config):
    login_page = LoginPage(page)
    base_url = config["base_url"]
    email = config["credentials"]["email"]
    password = config["credentials"]["password"]

    login_page.open(base_url)
    login_page.login(email, password)
    login_page.assert_logged_in()


@pytest.mark.regression
def test_login_invalid_credentials(page, config):
    login_page = LoginPage(page)
    base_url = config["base_url"]

    login_page.open(base_url)
    login_page.login("invalid@user.com", "wrongpass")
    login_page.assert_login_error()
