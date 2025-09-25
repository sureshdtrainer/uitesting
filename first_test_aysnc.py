import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")

        print(await page.title())

        # Wait for 3 seconds before closing the browser
        await asyncio.sleep(3)
        await browser.close()

asyncio.run(main())
