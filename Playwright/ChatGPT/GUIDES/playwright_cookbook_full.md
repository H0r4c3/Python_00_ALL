# Playwright Test Cookbook – PracticeSoftwareTesting.com  
_A complete, polished, production-ready guide_

---

# 📚 Table of Contents
1. [Overview](#overview)
2. [Selectors & Strategy](#selectors--strategy)
3. [Login Tests](#login-tests)
4. [Product Tests](#product-tests)
5. [Cart Tests](#cart-tests)
6. [Checkout Tests](#checkout-tests)
7. [Account Tests](#account-tests)
8. [Admin Tests](#admin-tests)
9. [End-to-End Scenario](#end-to-end-scenario)
10. [Best Practices](#best-practices)
11. [Debugging & Troubleshooting](#debugging--troubleshooting)
12. [VS Code Configuration](#vs-code-configuration)
13. [Recommended POM Structure](#recommended-pom-structure)

---

# Overview
This cookbook is tailored for **https://practicesoftwaretesting.com**, providing real-world Playwright + Pytest recipes.

---

# Selectors & Strategy
- Prefer `get_by_role` for stable selectors.
- Prefer `get_by_test_id` when available.
- Avoid brittle CSS when the DOM changes often.
- Use chained locators for component-level precision.

---

# Login Tests
```python
def test_login_success(page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.get_by_test_id("email").fill("customer@example.com")
    page.get_by_test_id("password").fill("customer")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/account")
    expect(page.get_by_text("Account")).to_be_visible()
```

```python
def test_login_invalid(page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.get_by_test_id("email").fill("wrong@example.com")
    page.get_by_test_id("password").fill("wrong")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Invalid credentials")).to_be_visible()
```

---

# Product Tests
```python
def test_filter_products(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.get_by_role("button", name="Filters").click()
    page.check("input[value='Electronics']")
    page.get_by_role("button", name="Apply").click()
    assert page.locator(".product-card").count() > 0
```

```python
def test_product_details(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.locator(".product-card").first.click()
    expect(page.get_by_role("heading")).to_contain_text("Product")
```

---

# Cart Tests
```python
def test_add_to_cart(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.locator(".product-card").first.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.locator(".cart-item")).to_have_count(1)
```

```python
def test_remove_from_cart(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.locator(".product-card").first.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="Remove").click()
    expect(page.locator(".cart-item")).to_have_count(0)
```

---

# Checkout Tests
```python
def test_checkout(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.locator(".product-card").first.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_test_id("firstname").fill("John")
    page.get_by_test_id("lastname").fill("Doe")
    page.get_by_test_id("address").fill("Test Street 1")
    page.get_by_role("button", name="Place Order").click()
    expect(page.get_by_text("Thank You")).to_be_visible()
```

---

# Account Tests
```python
def test_view_orders(page):
    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.get_by_test_id("email").fill("customer@example.com")
    page.get_by_test_id("password").fill("customer")
    page.get_by_role("button", name="Login").click()
    page.goto("https://practicesoftwaretesting.com/account/orders")
    expect(page.locator(".order-row")).to_be_visible()
```

---

# Admin Tests
```python
def test_admin_login(page):
    page.goto("https://practicesoftwaretesting.com/admin")
    page.fill("#email", "admin@example.com")
    page.fill("#password", "admin")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Dashboard")).to_be_visible()
```

---

# End-to-End Scenario
```python
def test_e2e(page):
    page.goto("https://practicesoftwaretesting.com/")
    page.locator(".product-card").nth(1).get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="Cart").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_test_id("firstname").fill("John")
    page.get_by_test_id("lastname").fill("Doe")
    page.get_by_test_id("address").fill("Street 1")
    page.get_by_role("button", name="Place Order").click()
    expect(page.get_by_text("Thank You")).to_be_visible()
```

---

# Best Practices
- Always use Playwright’s built-in waits.
- Avoid forcing timeouts.
- Prefer role-based locators.
- Use `expect()` for stability.
- Use POM for complex flows.

---

# Debugging & Troubleshooting
- Run with: `pytest --headed --slowmo 300`
- Use: `page.pause()` for inspector
- Use: `print(page.content())` when debugging DOM issues

---

# VS Code Configuration
Example `.vscode/settings.json`:

```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.defaultInterpreterPath": "venv-playwright/Scripts/python.exe"
}
```

---

# Recommended POM Structure
```
pages/
    login_page.py
    products_page.py
    cart_page.py
    checkout_page.py
    account_page.py
tests/
    test_login.py
    test_products.py
    test_cart.py
    test_checkout.py
    test_account.py
```
