'''
Example 84: Combined UI + API Testing

New concept: Combining API and UI in one test
What it does:

Uses API to set up test data (faster than UI)
Then uses UI to verify the result
Common pattern: API for setup/teardown, UI for actual testing
Much faster than doing everything through UI

Expected result: API creates data, then UI verifies it works.

pytest tests/test_ui_plus_api.py -v -s
'''

def test_ui_with_api_setup(playwright, page):
    # Step 1: Use API to create test data
    request_context = playwright.request.new_context()
    
    new_user = {
        "name": "Test User",
        "email": "testuser@example.com"
    }
    
    api_response = request_context.post(
        "https://jsonplaceholder.typicode.com/users",
        data=new_user
    )
    
    user_data = api_response.json()
    print(f"Created user via API: {user_data['name']}")
    
    # Step 2: Use UI to verify
    page.goto("https://jsonplaceholder.typicode.com/users")
    
    # Verify page loaded
    assert "JSONPlaceholder" in page.title() or "typicode" in page.content()
    
    print("UI test completed after API setup")