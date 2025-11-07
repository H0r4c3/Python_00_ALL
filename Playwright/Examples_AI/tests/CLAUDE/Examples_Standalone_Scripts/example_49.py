'''
Example 49: Upload a File
New instruction: page.set_input_files("input#file-upload", "example1.py")
What it does:
•	Finds a file upload input field
•	.set_input_files() selects a file to upload
•	"example1.py" the file path (must exist in your folder)
•	Like clicking "Choose File" and selecting a file
Expected result: You should see "example1.py" appear as the selected file (make sure the file exists!).

'''
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    page.set_input_files("input#file-upload", "example1.py")
    print("File selected for upload!")
    import time
    time.sleep(2)
    browser.close()
