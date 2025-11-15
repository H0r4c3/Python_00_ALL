"""Pytest configuration with all Page Object fixtures"""
import pytest
from pathlib import Path
from playwright.sync_api import Page

from pages.google_page import GooglePage
from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage
from pages.checkboxes_page import CheckboxesPage
from pages.tables_page import TablesPage
from pages.wikipedia_page import WikipediaPage
from pages.alerts_page import AlertsPage
from pages.windows_page import WindowsPage
from pages.drag_drop_page import DragDropPage
from pages.hovers_page import HoversPage


@pytest.fixture(scope="session")
def screenshots_dir():
    """Create screenshots directory"""
    screenshots = Path(__file__).parent / "screenshots"
    screenshots.mkdir(exist_ok=True)
    return screenshots


# Basic Page Object Fixtures
@pytest.fixture
def google_page(page: Page) -> GooglePage:
    """Provides GooglePage instance"""
    return GooglePage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provides LoginPage instance"""
    return LoginPage(page)


@pytest.fixture
def dropdown_page(page: Page) -> DropdownPage:
    """Provides DropdownPage instance"""
    return DropdownPage(page)


@pytest.fixture
def checkboxes_page(page: Page) -> CheckboxesPage:
    """Provides CheckboxesPage instance"""
    return CheckboxesPage(page)


@pytest.fixture
def tables_page(page: Page) -> TablesPage:
    """Provides TablesPage instance"""
    return TablesPage(page)


# Navigation Page Object Fixtures
@pytest.fixture
def wikipedia_page(page: Page) -> WikipediaPage:
    """Provides WikipediaPage instance"""
    return WikipediaPage(page)


# Advanced Page Object Fixtures
@pytest.fixture
def alerts_page(page: Page) -> AlertsPage:
    """Provides AlertsPage instance"""
    return AlertsPage(page)


@pytest.fixture
def windows_page(page: Page) -> WindowsPage:
    """Provides WindowsPage instance"""
    return WindowsPage(page)


@pytest.fixture
def drag_drop_page(page: Page) -> DragDropPage:
    """Provides DragDropPage instance"""
    return DragDropPage(page)


@pytest.fixture
def hovers_page(page: Page) -> HoversPage:
    """Provides HoversPage instance"""
    return HoversPage(page)


# Composite Fixtures
@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """Provides a page that's already logged in"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    return page


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request, screenshots_dir):
    """Take screenshot on test failure"""
    yield
    
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        screenshot_name = f"{request.node.name}.png"
        page.screenshot(path=screenshots_dir / screenshot_name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    
    
'''
## Complete File Structure

converted_examples/
├── __init__.py
├── conftest.py
├── pytest.ini
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── google_page.py
│   ├── login_page.py
│   ├── dropdown_page.py
│   ├── checkboxes_page.py
│   ├── tables_page.py
│   ├── wikipedia_page.py       # NEW
│   ├── alerts_page.py           # NEW
│   ├── windows_page.py          # NEW
│   ├── drag_drop_page.py        # NEW
│   └── hovers_page.py           # NEW
├── tests/
    ├── test_basics.py               # ✅ Has page objects
    ├── test_locators.py             # ✅ Has page objects
    ├── test_forms.py                # ✅ Has page objects
    ├── test_tables.py               # ✅ Has page objects
    ├── test_navigation.py           # ✅ NOW has page objects
    └── test_advanced.py             # ✅ NOW has page objects

Run All Tests:
# Run all tests with page objects
pytest converted_examples/ -v

# Run navigation tests
pytest converted_examples/test_navigation.py -v

# Run advanced tests
pytest converted_examples/test_advanced.py -v

# Run with HTML report
pytest converted_examples/ -v --html=report.html --self-contained-html

# Run in parallel
pytest converted_examples/ -v -n auto

'''