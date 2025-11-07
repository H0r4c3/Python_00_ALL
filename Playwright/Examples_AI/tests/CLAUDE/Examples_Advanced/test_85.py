'''
Example 85: Running Tests in Parallel

First, install pytest-xdist:
pip install pytest-xdist

Run normally (sequential):
pytest tests/test_parallel.py -v -s
This will take ~8+ seconds (one after another).

Run in parallel:
pytest tests/test_parallel.py -v -s -n auto

New instruction: -n auto
What it does:

-n auto runs tests in parallel using all CPU cores
Each test runs in its own browser instance
Much faster for large test suites
-n 2 runs 2 tests at once, -n 4 runs 4, etc.

Expected result: Tests finish in ~2-3 seconds instead of 8! All run at the same time.
'''

import time

def test_parallel_1(page):
    page.goto("https://the-internet.herokuapp.com/login")
    time.sleep(2)  # Simulate slow test
    assert "Login Page" in page.inner_text("h2")
    print("Test 1 finished")

def test_parallel_2(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(2)  # Simulate slow test
    assert "Checkboxes" in page.inner_text("h3")
    print("Test 2 finished")

def test_parallel_3(page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    time.sleep(2)  # Simulate slow test
    assert "Dropdown List" in page.inner_text("h3")
    print("Test 3 finished")

def test_parallel_4(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    time.sleep(2)  # Simulate slow test
    assert "Hovers" in page.inner_text("h3")
    print("Test 4 finished")