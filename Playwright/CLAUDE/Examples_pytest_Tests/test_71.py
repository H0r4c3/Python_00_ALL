from playwright.sync_api import expect

def test_google_title(page):
    page.goto("https://www.google.com")
    #assert "Google" in page.title()
    expect(page).to_have_title("Google")