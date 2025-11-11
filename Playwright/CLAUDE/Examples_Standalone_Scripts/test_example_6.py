'''
Example 6: Get Page Title
New instruction: title = page.title()
What it does:
•	Gets the title of the webpage
•	The title is what you see in the browser tab at the top
•	Stores it in variable title so we can print it
Expected result: You see in the terminal something like: Page title is: Google

'''

from playwright.sync_api import Page, expect

def test_homepage_title(page: Page) -> None:
    """Test homepage has correct title"""
    page.goto("https://practicesoftwaretesting.com/")
    expect(page).to_have_title('Practice Software Testing - Toolshop - v5.0')



