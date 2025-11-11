'''
Example 90: Advanced Test - Combining Everything! 🎉
This final example combines: UI + API + Database + POM + Parallel execution

This example combines:

✅ Database fixture (test_db)
✅ Page Object Model (login_page)
✅ API testing (playwright.request)
✅ Visual regression (to_have_screenshot)
✅ UI automation
✅ Ready for parallel execution


Run sequentially:
bashpytest tests/test_advanced_complete.py -v -s
Run in parallel:
bashpytest tests/test_advanced_complete.py -v -s -n auto
Generate HTML report:
bashpytest tests/test_advanced_complete.py -v --html=advanced-report.html --self-contained-html

Expected result: All 4 tests pass showing complete integration!

'''

from playwright.sync_api import expect
import time

def test_complete_user_flow_with_db(test_db, login_page, playwright):
    """Complete test: DB setup → API verification → UI testing"""
    
    # Step 1: Get user from database
    cursor = test_db.cursor()
    cursor.execute("SELECT username, email FROM users WHERE username = ?", ("tomsmith",))
    db_user = cursor.fetchone()
    print(f"Step 1: Retrieved user from DB: {db_user[0]}")
    
    # Step 2: Verify user via API (simulated)
    request_context = playwright.request.new_context()
    api_response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    assert api_response.ok
    print(f"Step 2: API check passed with status {api_response.status}")
    
    # Step 3: UI test using Page Object Model
    login_page.navigate()
    login_page.login(db_user[0], "SuperSecretPassword!")
    
    # Step 4: Visual regression check
    expect(login_page.page).to_have_screenshot("complete-flow-result.png", max_diff_pixels=100)
    
    # Step 5: Verify success
    assert login_page.is_login_successful()
    print("Step 3-5: UI login successful, visual check passed")
    
    # Step 6: Update database after successful login
    cursor.execute("UPDATE users SET is_active = 1 WHERE username = ?", (db_user[0],))
    test_db.commit()
    
    cursor.execute("SELECT is_active FROM users WHERE username = ?", (db_user[0],))
    is_active = cursor.fetchone()[0]
    assert is_active == 1
    print("Step 6: Database updated successfully")

def test_parallel_flow_1(page, playwright):
    """First parallel test - API + UI"""
    request_context = playwright.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.ok
    
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.check("input[type='checkbox']")
    assert page.locator("input[type='checkbox']").first.is_checked()
    print("Parallel test 1 completed")

def test_parallel_flow_2(page):
    """Second parallel test - UI only"""
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("select#dropdown", "1")
    assert page.locator("select#dropdown").input_value() == "1"
    print("Parallel test 2 completed")

def test_parallel_flow_3(playwright):
    """Third parallel test - API only"""
    request_context = playwright.request.new_context()
    
    new_post = {"title": "Test", "body": "Content", "userId": 1}
    response = request_context.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=new_post
    )
    assert response.status == 201
    print("Parallel test 3 completed")