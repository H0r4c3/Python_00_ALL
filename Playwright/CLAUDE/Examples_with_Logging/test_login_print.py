
from playwright.sync_api import Page

def test_login(page: Page) -> None:
    print("▶️ Test started")
    
    print("📍 Navigating...")
    page.goto("https://example.com")
    
    print("📍 Filling form...")
    page.fill("#username", "user")
    page.fill("#password", "pass")
    
    print("📍 Submitting...")
    page.click("#login")
    
    print("✅ Done!")