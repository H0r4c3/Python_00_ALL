'''
async_playwright()

async with async_playwright() as p:   ->   Start Playwright, give me access to browsers
'''

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        print("Playwright is ready!")

asyncio.run(main())
