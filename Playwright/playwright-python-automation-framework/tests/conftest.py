import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright, Browser, APIRequestContext
from utils.config_loader import load_config


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, config) -> Browser:
    """Single browser instance for the full test session."""
    headless = config.get("headless", True)
    slow_mo = config.get("slow_mo", 0)
    browser = playwright_instance.chromium.launch(headless=headless, slow_mo=slow_mo)
    yield browser
    browser.close()


@pytest.fixture
def context(browser, config):
    """New context per test for isolation. Reuses auth_state if configured."""
    auth_state = config.get("auth_state")
    if auth_state:
        context = browser.new_context(storage_state=auth_state)
    else:
        context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page


@pytest.fixture(scope="session")
def request_context(playwright_instance, config) -> APIRequestContext:
    """APIRequestContext for API tests."""
    base_url = config.get("base_url")
    request = playwright_instance.request.new_context(base_url=base_url)
    yield request
    request.dispose()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on failure and attach into pytest-html report if present."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            file_name = f"{item.name}.png"
            dest = screenshots_dir / file_name
            page.screenshot(path=str(dest))

            # Attach to pytest-html if plugin is available
            try:
                from pytest_html import extras  # type: ignore
                if hasattr(report, "extra"):
                    report.extra.append(extras.image(str(dest)))
            except Exception:
                # If pytest-html not installed or any error, ignore gracefully
                pass
