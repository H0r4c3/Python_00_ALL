# Playwright Python + Pytest — COMPACT VERSION

A short, essential reference.

---

## Navigation (4)
- `page.goto(url)`
- `page.reload()`
- `page.go_back()`
- `page.set_viewport_size({"width":1280,"height":720})`

---

## Locators (4)
- `page.locator("css")`
- `page.get_by_text("Login")`
- `page.get_by_role("button", name="Submit")`
- `page.get_by_test_id("email-input")`

---

## Actions (6)
- click: `page.click("#btn")`
- fill: `page.fill("#email","a@b.com")`
- type: `page.type("#search","Playwright")`
- select: `page.select_option("#country","RO")`
- hover: `page.hover(".item")`
- upload: `page.set_input_files("#file","a.txt")`

---

## Assertions (6)
- `expect(page).to_have_title()`
- `expect(page).to_have_url()`
- `expect(locator).to_be_visible()`
- `expect(locator).to_have_text()`
- `expect(locator).to_have_count(5)`
- `expect(locator).to_be_enabled()`

---

## Waits (4)
- `page.wait_for_selector()`
- `page.wait_for_url()`
- `page.wait_for_response()`
- `page.wait_for_timeout()`

---

## Screenshots (2)
- full page: `page.screenshot(path="p.png", full_page=True)`
- element: `page.locator("h1").screenshot(path="h1.png")`

---

## Page Content (4)
- `locator.text_content()`
- `locator.get_attribute()`
- `locator.input_value()`
- `page.content()`

---

## Advanced (6)
- dialog: `page.once("dialog", lambda d: d.accept())`
- route: `page.route("**/*",lambda r:r.continue_())`
- cookies: `context.add_cookies([...])`
- frames: `page.frame(name="login")`
- geolocation: `browser.new_context(geolocation={"latitude":1,"longitude":2})`
- API: `api.get("https://example.com")`

---

# END OF COMPACT VERSION
