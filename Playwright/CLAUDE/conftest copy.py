"""
Global conftest.py - Shared fixtures and hooks for ALL tests

What it does:
- Provides reusable fixtures available to ALL test files automatically
- No need to import fixtures - pytest finds them automatically
- Adds beautiful test execution banners with timestamps
- Shows test results (PASS/FAIL) in real-time
- Works across all test directories (ChatGPT, CLAUDE, eztv, etc.)

Structure:
- One conftest.py in project root = applies to ALL tests
- Can add directory-specific conftest.py for custom behavior
- Fixtures cascade: root fixtures available everywhere
"""

import pytest
from datetime import datetime
from pathlib import Path

# ============================================================================
# PYTEST CONFIGURATION - Timestamped Results
# ============================================================================

def pytest_configure(config):
    """
    Create timestamped results directory before tests run.
    This keeps history of all test runs.
    """
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create timestamped results folder
    results_base = Path("results_Playwright")
    results_dir = results_base / timestamp
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # Update config to use timestamped paths
    # HTML Report
    if config.option.htmlpath:
        config.option.htmlpath = str(results_dir / "test-report.html")
    
    # Playwright output
    if hasattr(config.option, 'output'):
        config.option.output = str(results_dir / "playwright-results")
    
    # Log file - THIS WAS MISSING!
    config.option.log_file = str(results_dir / "test-logs.log")
    
    # Store for later use
    config.results_dir = results_dir
    
    print(f"\n📁 Results will be saved to: {results_dir}\n")


# ============================================================================
# PYTEST HOOKS - Test Execution Reporting
# ============================================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    """
    Hook that runs BEFORE and AFTER each test.
    Prints beautiful banners showing test progress in real-time.
    """
    # BEFORE test runs
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"\n{'='*70}")
    print(f"🧪 STARTING TEST: {item.nodeid}")
    print(f"⏰ Time: {timestamp}")
    print(f"{'='*70}\n")
    
    # Let the test run
    yield
    
    # AFTER test completes (this won't show pass/fail accurately)
    # We'll use pytest_runtest_makereport instead for accurate results


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that captures test results and shows PASS/FAIL status.
    More accurate than pytest_runtest_protocol for showing results.
    """
    outcome = yield
    report = outcome.get_result()
    
    # Only report on the actual test call (not setup/teardown)
    if report.when == "call":
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if report.passed:
            print(f"\n{'='*70}")
            print(f"✅ PASSED: {item.name}")
            print(f"⏰ Time: {timestamp}")
            print(f"{'='*70}\n")
        elif report.failed:
            print(f"\n{'='*70}")
            print(f"❌ FAILED: {item.name}")
            print(f"⏰ Time: {timestamp}")
            print(f"{'='*70}\n")
        elif report.skipped:
            print(f"\n{'='*70}")
            print(f"⏭️  SKIPPED: {item.name}")
            print(f"⏰ Time: {timestamp}")
            print(f"{'='*70}\n")


# ============================================================================
# SHARED FIXTURES - Available to ALL tests
# ============================================================================

# Example: Remove the fixtures below if they're not applicable to all projects
# Keep them if you want login_page available across ChatGPT, CLAUDE, eztv tests

# Uncomment and modify if you have a shared login page across projects:
# @pytest.fixture
# def login_page(page):
#     """Provides a LoginPage instance - available to ALL tests"""
#     from pages.login_page import LoginPage
#     return LoginPage(page)

# @pytest.fixture
# def logged_in_page(page):
#     """Provides a page that's already logged in - available to ALL tests"""
#     from pages.login_page import LoginPage
#     login_page = LoginPage(page)
#     login_page.navigate()
#     login_page.login("tomsmith", "SuperSecretPassword!")
#     return page


# ============================================================================
# DIRECTORY-SPECIFIC FIXTURES
# ============================================================================
# If you need fixtures specific to ChatGPT, CLAUDE, or eztv:
# Create a conftest.py in that directory with those fixtures
# Example: ChatGPT/conftest.py can have ChatGPT-specific fixtures

'''
## **Key Improvements:**

### ✅ **Better Result Reporting**
- Uses `pytest_runtest_makereport` for accurate PASS/FAIL/SKIP status
- Shows results immediately after each test completes

### ✅ **Root-Level Ready**
- Works across ALL your test directories (ChatGPT, CLAUDE, eztv)
- Clear documentation for team members
- Commented out project-specific fixtures (login_page) - uncomment if needed

### ✅ **Better Hook Implementation**
- Uses `@pytest.hookimpl(hookwrapper=True)` for both hooks
- Cleaner separation: protocol for start banner, makereport for results

### ✅ **Full Node ID in Output**
Shows complete test path: `ChatGPT/test_something.py::test_login` so you know exactly which test is running

## **What You'll See:**
```
======================================================================
🧪 STARTING TEST: ChatGPT/test_login.py::test_login
⏰ Time: 14:23:45
======================================================================

📍 Step 1: Navigate to login page
📍 Step 2: Fill credentials
📍 Step 3: Click login
📍 Step 4: Verify success

======================================================================
✅ PASSED: test_login
⏰ Time: 14:23:50
======================================================================
'''