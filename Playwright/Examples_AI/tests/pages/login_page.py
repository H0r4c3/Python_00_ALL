class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.success_message = page.locator("#flash")
        
    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")
        
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def is_login_successful(self):
        return "You logged into a secure area!" in self.success_message.inner_text()
        
    def get_error_message(self):
        return self.success_message.inner_text()