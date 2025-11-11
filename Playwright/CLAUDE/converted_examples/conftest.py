"""Pytest configuration with Page Object fixtures"""
import pytest
from pathlib import Path
from playwright.sync_api import Page

from pages.google_page import GooglePage
from pages.login_page import LoginPage
from pages.dropdown_page import DropdownPage
from pages.checkboxes_page import CheckboxesPage
from pages.tables_page import TablesPage


@pytest.fixture(scope="session")
def screenshots_dir():
    """Create screenshots directory"""
    screenshots = Path(__file__).parent / "screenshots"
    screenshots.mkdir(exist_ok=True)
    return screenshots


# Page Object Fixtures
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