'''
Example 76: Skip and XFail Tests

New instruction: @pytest.mark.skip(), @pytest.mark.skipif(), @pytest.mark.xfail()
What it does:

@pytest.mark.skip() - completely skips the test (never runs)
@pytest.mark.skipif(condition) - skips if condition is True
@pytest.mark.xfail() - runs test but expects it to fail (useful for known bugs)

Expected result:

2 tests SKIPPED
1 test XFAIL (expected failure)
1 test PASSED

'''

import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_feature_not_ready(page):
    page.goto("https://the-internet.herokuapp.com/login")
    # This test won't run at all
    assert False

@pytest.mark.skipif(True, reason="Only run in production")
def test_skip_conditionally(page):
    page.goto("https://the-internet.herokuapp.com/login")
    # Skipped because condition is True
    assert False

@pytest.mark.xfail(reason="Known bug in application")
def test_expected_to_fail(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_label("Username").fill("tomsmith")
    # This assertion will fail, but test is marked as "expected fail"
    assert "Wrong Text" in page.inner_text("body")

def test_normal_test(page):
    page.goto("https://the-internet.herokuapp.com/login")
    assert "Login Page" in page.inner_text("body")