'''
Example 87: Visual Regression Testing (Screenshot Comparison)
Playwright can compare screenshots to detect visual changes!

New instruction: expect(page).to_have_screenshot("name.png")
What it does:

First run: Creates baseline screenshots (golden images)
Future runs: Compares current screenshot with baseline
If different: Test fails and shows differences
Catches visual bugs (CSS changes, layout breaks, missing images)

Expected result:

First run: Creates baseline screenshots (tests pass)
If page changes: Tests fail showing visual differences

Run it (first time to create baselines):
bashpytest tests/test_visual_regression.py -v
Run it again (should pass - no changes):
bashpytest tests/test_visual_regression.py -v
To update baselines (when you want to accept changes):
bashpytest tests/test_visual_regression.py -v --update-snapshots
'''
from playwright.sync_api import expect

def test_visual_regression_login_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # First run: creates baseline screenshot
    # Next runs: compares against baseline
    page.screenshot(path="tests/screenshots/login-page.png")
    
    # Use Playwright's built-in visual comparison
    expect(page).to_have_screenshot("login-page-baseline.png")

def test_visual_element_regression(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Take screenshot of specific element
    login_form = page.locator("#login")
    expect(login_form).to_have_screenshot("login-form-baseline.png")
    
def test_visual_regression_full_page(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Compare full page screenshot
    expect(page).to_have_screenshot("login-page-full.png")

def test_visual_regression_element(page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Compare specific element
    login_box = page.locator("#content")
    expect(login_box).to_have_screenshot("login-box.png")