import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

def test_login(page: Page) -> None:
    logger.info("▶️ Starting login test")
    
    logger.info("📍 Step 1: Navigate to login page")
    page.goto("https://example.com")
    
    logger.info("📍 Step 2: Fill credentials")
    page.fill("#username", "user")
    page.fill("#password", "pass")
    
    logger.info("📍 Step 3: Click login")
    page.click("#login")
    
    logger.info("📍 Step 4: Verify success")
    assert "dashboard" in page.url
    
    logger.info("✅ Test passed!")