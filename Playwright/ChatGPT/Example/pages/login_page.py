from playwright.sync_api import Page, expect
import time

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.signin_button = page.locator("[data-test=\"nav-sign-in\"]")
        
        self.username_input = page.locator("[data-test=\"email\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-submit\"]")

    def open(self):
        self.page.goto("https://practicesoftwaretesting.com")
        time.sleep(3)
        self.signin_button.click()
        

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        time.sleep(3)
        self.login_button.click()

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://practicesoftwaretesting.com/account")
