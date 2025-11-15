from playwright.sync_api import Page
import time

#from pages.login_page import LoginPage
from ChatGPT.Example.pages.login_page import LoginPage


# USERNAME = customer@practicesoftwaretesting.com
# password = welcome01
# https://github.com/testsmith-io/practice-software-testing

def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    time.sleep(3)
    login_page.login("customer@practicesoftwaretesting.com", "welcome01")
    time.sleep(3)
    login_page.assert_login_successful()
