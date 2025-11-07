'''
Run in Terminal from Playwright folder:
pytest tests/CLAUDE/Examples_pytest_Tests/test_80.py -v --html=report.html --self-contained-html

Run from anywhere:
cd C:\Users\Horace.000\eclipse-workspace\Python_Project_6_Online_Courses\00_ALL\Playwright
pytest tests/CLAUDE/Examples_pytest_Tests/test_80.py -v --html=report.html --self-contained-html
'''

import subprocess
import webbrowser
import os

# Run pytest with HTML report
print("Running tests and generating report...")
result = subprocess.run([
    "pytest",
    "tests/CLAUDE/Examples_pytest_Tests/test_80.py",
    "-v",
    "--html=report.html",
    "--self-contained-html"
], capture_output=True, text=True)

# Print output
print(result.stdout)
print(result.stderr)

# Open report in browser if it exists
if os.path.exists("report.html"):
    print("\nOpening report in browser...")
    webbrowser.open("report.html")
else:
    print("\nReport not generated.")