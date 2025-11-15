"""
Base conftest.py - Minimal essential hooks for most projects
Customize by adding project-specific fixtures below
"""

import pytest
from datetime import datetime
from pathlib import Path

# ============================================================================
# TIMESTAMPED RESULTS - Universal for all projects
# ============================================================================

def pytest_configure(config):
    """Create timestamped results directory - works for any project"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    results_base = Path("test_results")  # Standard name
    results_dir = results_base / timestamp
    results_dir.mkdir(parents=True, exist_ok=True)
    
    # HTML Report (if pytest-html installed)
    if hasattr(config.option, 'htmlpath') and config.option.htmlpath:
        config.option.htmlpath = str(results_dir / "test-report.html")
    
    # Log file
    if hasattr(config.option, 'log_file'):
        config.option.log_file = str(results_dir / "test-logs.log")
    
    config.results_dir = results_dir
    print(f"\n📁 Results: {results_dir}\n")


# ============================================================================
# TEST EXECUTION HOOKS - Universal reporting
# ============================================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    """Print test start banner"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"\n{'='*70}")
    print(f"🧪 [{timestamp}] STARTING: {item.nodeid}")
    print(f"{'='*70}\n")
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Print test result"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        timestamp = datetime.now().strftime("%H:%M:%S")
        symbol = "✅" if report.passed else "❌" if report.failed else "⏭️"
        status = "PASSED" if report.passed else "FAILED" if report.failed else "SKIPPED"
        
        print(f"\n{'='*70}")
        print(f"{symbol} [{timestamp}] {status}: {item.name}")
        if hasattr(item.config, 'results_dir'):
            print(f"📁 Results: {item.config.results_dir}")
        print(f"{'='*70}\n")


# ============================================================================
# PROJECT-SPECIFIC FIXTURES - Add your fixtures below
# ============================================================================

# Example: Playwright fixtures (uncomment if using Playwright)
# @pytest.fixture
# def browser_context_args(browser_context_args):
#     return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}

# Example: API testing fixtures (uncomment if testing APIs)
# @pytest.fixture
# def api_client():
#     import requests
#     return requests.Session()

# Example: Database fixtures (uncomment if using databases)
# @pytest.fixture
# def db_connection():
#     # Setup database
#     yield connection
#     # Teardown database