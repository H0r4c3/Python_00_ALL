'''
Example 82: API Testing with Playwright
Playwright can test APIs too, not just UI!

New instruction: playwright.request.new_context() and request_context.get()
What it does:

Creates an API request context (separate from browser)
request_context.get() makes a GET request
response.json() parses JSON response
Test APIs without opening a browser!

Run it in Terminal:

pytest tests/test_api.py -v -s

The -s flag shows the print output.

Expected result: API test passes, prints post title.
'''

def test_api_get_request(playwright):
    request_context = playwright.request.new_context()
    
    # Make GET request
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Assertions
    assert response.status == 200
    assert response.ok
    
    # Get JSON data
    data = response.json()
    assert data["userId"] == 1
    assert data["id"] == 1
    assert "title" in data
    
    print(f"Post title: {data['title']}")