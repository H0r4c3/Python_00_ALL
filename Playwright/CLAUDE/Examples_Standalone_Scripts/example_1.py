'''
What it does: Only imports and starts Playwright. That's all.

New instruction: from playwright.sync_api import sync_playwright and with sync_playwright() as p:
What it does:
•	Imports the Playwright library (sync version)
•	with sync_playwright() as p: starts Playwright and stores it in variable p
•	The with statement ensures Playwright closes properly when done
Expected result: You see "Playwright started!" printed in the terminal.

'''

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print("Playwright started!")