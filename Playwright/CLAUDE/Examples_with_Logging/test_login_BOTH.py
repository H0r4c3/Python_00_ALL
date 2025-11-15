import logging
from playwright.sync_api import Page

logger = logging.getLogger(__name__)

def test_login(page: Page) -> None:
    print("📍 Step 1: Navigate to login page")
    logger.info("📍 Step 1: Navigate to login page")
    page.goto("https://the-internet.herokuapp.com/login")
    
    print("📍 Step 2: Fill credentials")
    logger.info("📍 Step 2: Fill credentials")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    
    print("📍 Step 3: Click login")
    logger.info("📍 Step 3: Click login")
    page.click("button[type='submit']")
    
    print("📍 Step 4: Verify success")
    logger.info("📍 Step 4: Verify success")
    assert "secure" in page.url
    
    print("✅ All steps completed!")
    logger.info("✅ All steps completed!")
    
    
'''
### **After running `pytest`:**
```
your_project/
├── CLAUDE/
│   ├── test_login.py
│   └── results/                    ← Results here!
│       ├── test-report.html
│       ├── test-logs.log
│       └── test-results/


## **What You'll See When Running:**

======================================================================
🧪 [14:23:45] STARTING: test_login
======================================================================

📍 Step 1: Navigate to login page
2025-11-13 14:23:45 [    INFO] 📍 Step 1: Navigate to login page
📍 Step 2: Fill credentials
2025-11-13 14:23:46 [    INFO] 📍 Step 2: Fill credentials
📍 Step 3: Click login
2025-11-13 14:23:47 [    INFO] 📍 Step 3: Click login
📍 Step 4: Verify success
2025-11-13 14:23:48 [    INFO] 📍 Step 4: Verify success
✅ All steps completed!
2025-11-13 14:23:48 [    INFO] ✅ All steps completed!

✅ [14:23:48] PASSED: test_login
'''