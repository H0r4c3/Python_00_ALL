from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://practicesoftwaretesting.com/")
        page.get_by_role("link", name="My account").click()

        page.get_by_label("Email").fill("customer@practicesoftwaretesting.com")
        page.get_by_label("Password").fill("welcome01")
        page.get_by_role("button", name="Login").click()

        context.storage_state(path="auth_state.json")
        print("auth_state.json saved in project root")

        context.close()
        browser.close()


if __name__ == "__main__":
    run()
