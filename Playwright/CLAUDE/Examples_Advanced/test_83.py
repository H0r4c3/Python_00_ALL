'''
Example 83: API POST Request


'''

def test_api_post_request(playwright):
    request_context = playwright.request.new_context()
    
    # Data to send
    new_post = {
        "title": "My Test Post",
        "body": "This is test content",
        "userId": 1
    }
    
    # Make POST request
    response = request_context.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=new_post
    )
    
    # Assertions
    assert response.status == 201  # 201 = Created
    assert response.ok
    
    # Check response
    data = response.json()
    assert data["title"] == "My Test Post"
    assert data["body"] == "This is test content"
    assert data["userId"] == 1
    assert "id" in data  # Server assigns an ID
    
    print(f"Created post with ID: {data['id']}")