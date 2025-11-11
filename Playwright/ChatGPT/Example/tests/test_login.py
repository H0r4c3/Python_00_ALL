from playwright.sync_api import Page
#from pages.login_page import LoginPage
from ChatGPT.pages.login_page import LoginPage

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("customer", "welcome01")
    login_page.assert_login_successful()
