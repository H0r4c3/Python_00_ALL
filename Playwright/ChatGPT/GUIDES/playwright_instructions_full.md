# Playwright Python + Pytest — FULL VERSION (100 Instructions)

This document contains all 100 Playwright instructions grouped by category.
Each instruction includes:
- What it does
- Expected result
- Pytest example

---

## 📍 Navigation & Page Operations (8)

### Instruction 1: Go to URL
**What it does:** Navigates to a given webpage.  
**Expected result:** Page loads successfully.  
```python
def test_go_to(page):
    page.goto("https://example.com")
    expect(page).to_have_url("https://example.com/")
```

### Instruction 2: Reload Page
Reloads the current page.  
```python
page.reload()
```

### Instruction 3: Go Back  
```python
page.go_back()
```

### Instruction 4: Go Forward  
```python
page.go_forward()
```

### Instruction 5: Set Viewport  
```python
page.set_viewport_size({"width": 1280, "height": 720})
```

### Instruction 6: Wait for Load State  
```python
page.wait_for_load_state("networkidle")
```

### Instruction 7: New Browser Context  
```python
context = browser.new_context()
```

### Instruction 8: New Page  
```python
page = context.new_page()
```

---

## 🎯 Locators & Finding Elements (14)

### Instruction 9: Locate by CSS  
```python
button = page.locator("button.submit")
```

### Instruction 10: Locate by Text  
```python
page.get_by_text("Login")
```

### Instruction 11: Locate by Role  
```python
page.get_by_role("button", name="Submit")
```

### Instruction 12: Locate by Test ID  
```python
page.get_by_test_id("email-input")
```

### Instruction 13: Locate by XPath  
```python
page.locator("//div[@id='header']")
```

### Instruction 14: nth() Locator  
```python
page.locator("button").nth(2)
```

### Instruction 15: Filter Locator  
```python
page.locator("button").filter(has_text="Add")
```

### Instruction 16: First Element  
```python
page.locator("li").first
```

### Instruction 17: Last Element  
```python
page.locator("li").last
```

### Instruction 18: Get Inner Text  
```python
page.locator("h1").inner_text()
```

### Instruction 19: Get Inner HTML  
```python
page.locator("div").inner_html()
```

### Instruction 20: Count Elements  
```python
page.locator("li").count()
```

### Instruction 21: Has Locator  
```python
page.locator("form").filter(has=page.locator("input#email"))
```

### Instruction 22: Locator Wait  
```python
page.locator("button").wait_for()
```

---

## 🖱️ Interactions & Actions (15)

### Instruction 23: Click  
```python
page.get_by_role("button").click()
```

### Instruction 24: Fill  
```python
page.fill("#email", "test@example.com")
```

### Instruction 25: Type  
```python
page.type("#search", "Playwright")
```

### Instruction 26: Press Key  
```python
page.press("#search", "Enter")
```

### Instruction 27: Check Checkbox  
```python
page.check("#accept")
```

### Instruction 28: Uncheck  
```python
page.uncheck("#subscribe")
```

### Instruction 29: Select Dropdown  
```python
page.select_option("#country", "RO")
```

### Instruction 30: Hover  
```python
page.hover(".menu-item")
```

### Instruction 31: Drag & Drop  
```python
page.drag_and_drop("#from", "#to")
```

### Instruction 32: Double Click  
```python
page.dblclick("#edit")
```

### Instruction 33: Right Click  
```python
page.click("#target", button="right")
```

### Instruction 34: Scroll  
```python
page.mouse.wheel(0, 800)
```

### Instruction 35: Focus  
```python
page.focus("#email")
```

### Instruction 36: Blur  
```python
page.locator("#email").blur()
```

### Instruction 37: Upload File  
```python
page.set_input_files("#upload", "file.txt")
```

---

## ✅ Assertions & Expectations (16)

### Instruction 38: Expect Title  
```python
expect(page).to_have_title("Dashboard")
```

### Instruction 39: Expect URL  
```python
expect(page).to_have_url("https://example.com/home")
```

### Instruction 40: Expect Visible  
```python
expect(page.locator("#login")).to_be_visible()
```

### Instruction 41: Expect Hidden  
```python
expect(page.locator("#loader")).to_be_hidden()
```

### Instruction 42: Expect Text  
```python
expect(page.locator("h1")).to_have_text("Welcome")
```

### Instruction 43: Expect Attribute  
```python
expect(page.locator("input")).to_have_attribute("type", "text")
```

### Instruction 44: Expect Count  
```python
expect(page.locator("li")).to_have_count(5)
```

### Instruction 45: Expect Enabled  
```python
expect(page.locator("#submit")).to_be_enabled()
```

### Instruction 46: Expect Disabled  
```python
expect(page.locator("#submit")).to_be_disabled()
```

### Instruction 47: Expect Checked  
```python
expect(page.locator("#terms")).to_be_checked()
```

### Instruction 48: Expect Unchecked  
```python
expect(page.locator("#terms")).not_to_be_checked()
```

### Instruction 49: Expect Editable  
```python
expect(page.locator("#email")).to_be_editable()
```

### Instruction 50: Expect Not Editable  
```python
expect(page.locator("#email")).not_to_be_editable()
```

### Instruction 51: Expect CSS  
```python
expect(page.locator("h1")).to_have_css("color", "rgb(0, 0, 0)")
```

### Instruction 52: Expect Screenshot Match  
```python
expect(page).to_have_screenshot()
```

### Instruction 53: Expect JS Expression  
```python
expect(page.evaluate("2 + 2")).to_be(4)
```

---

## ⏱️ Waits & Timeouts (7)

### Instruction 54: Wait for Selector  
```python
page.wait_for_selector("#dashboard")
```

### Instruction 55: Wait for URL  
```python
page.wait_for_url("**/home")
```

### Instruction 56: Wait for Response  
```python
page.wait_for_response("**/api/login")
```

### Instruction 57: Wait for Timeout  
```python
page.wait_for_timeout(1000)
```

### Instruction 58: Wait for Function  
```python
page.wait_for_function("window.appReady === true")
```

### Instruction 59: Set Default Timeout  
```python
page.set_default_timeout(8000)
```

### Instruction 60: Set Navigation Timeout  
```python
page.set_default_navigation_timeout(10000)
```

---

## 📸 Screenshots & Recordings (3)

### Instruction 61: Full Page Screenshot  
```python
page.screenshot(path="page.png", full_page=True)
```

### Instruction 62: Element Screenshot  
```python
page.locator("h1").screenshot(path="title.png")
```

### Instruction 63: Video Recording (context)  
```python
context = browser.new_context(record_video_dir="videos/")
```

---

## 📄 Page Content & Properties (9)

### Instruction 64: Get Text Content  
```python
page.locator("h1").text_content()
```

### Instruction 65: Get Attribute  
```python
page.locator("#email").get_attribute("placeholder")
```

### Instruction 66: Get Input Value  
```python
page.locator("#email").input_value()
```

### Instruction 67: Is Visible  
```python
page.locator("#menu").is_visible()
```

### Instruction 68: Is Enabled  
```python
page.locator("#submit").is_enabled()
```

### Instruction 69: Is Checked  
```python
page.locator("#agree").is_checked()
```

### Instruction 70: Title  
```python
title = page.title()
```

### Instruction 71: URL  
```python
page.url
```

### Instruction 72: Content HTML  
```python
page.content()
```

---

## 🔄 Advanced Operations (28)

### Instruction 73: Handle Dialog  
```python
page.once("dialog", lambda dialog: dialog.accept())
```

### Instruction 74: Route Intercept  
```python
page.route("**/api/*", lambda r: r.continue_())
```

### Instruction 75: Modify Response  
```python
page.route("**/api/data", lambda r: r.fulfill(body='{"ok": true}'))
```

### Instruction 76: Evaluate JS  
```python
page.evaluate("() => document.body.style.background = 'red'")
```

### Instruction 77: Add Script Tag  
```python
page.add_script_tag(url="https://example.com/script.js")
```

### Instruction 78: Add Style Tag  
```python
page.add_style_tag(content="body { color: red }")
```

### Instruction 79: Cookie Set  
```python
context.add_cookies([{"name": "session", "value": "abc", "url": "https://example.com"}])
```

### Instruction 80: Get Cookies  
```python
context.cookies()
```

### Instruction 81: Storage State  
```python
context.storage_state(path="state.json")
```

### Instruction 82: Load Storage State  
```python
browser.new_context(storage_state="state.json")
```

### Instruction 83: File Download  
```python
with page.expect_download() as download_info:
    page.click("#download")
download = download_info.value
download.save_as("file.zip")
```

### Instruction 84: File Upload (Drag)  
```python
page.locator("#upload").set_input_files(["a.txt"])
```

### Instruction 85: Mouse Move  
```python
page.mouse.move(100, 200)
```

### Instruction 86: Mouse Click  
```python
page.mouse.click(100, 200)
```

### Instruction 87: Mouse Down  
```python
page.mouse.down()
```

### Instruction 88: Mouse Up  
```python
page.mouse.up()
```

### Instruction 89: Keyboard Type  
```python
page.keyboard.type("Hello")
```

### Instruction 90: Keyboard Press  
```python
page.keyboard.press("Enter")
```

### Instruction 91: Frame Locator  
```python
page.frame_locator("#myframe").locator("button").click()
```

### Instruction 92: Get Frame by Name  
```python
frame = page.frame(name="loginFrame")
```

### Instruction 93: Emulate Geolocation  
```python
context = browser.new_context(geolocation={"longitude": 10, "latitude": 20})
```

### Instruction 94: Emulate Online/Offline  
```python
context.set_offline(True)
```

### Instruction 95: Set User Agent  
```python
browser.new_context(user_agent="CustomAgent/1.0")
```

### Instruction 96: Set Locale  
```python
browser.new_context(locale="ro-RO")
```

### Instruction 97: Emulate Dark Mode  
```python
browser.new_context(color_scheme="dark")
```

### Instruction 98: HTTP Credentials  
```python
browser.new_context(http_credentials={"username": "admin", "password": "admin"})
```

### Instruction 99: Request Context  
```python
api = playwright.request.new_context()
```

### Instruction 100: API Request  
```python
response = api.get("https://example.com/api")
```

---

# END OF FULL VERSION
