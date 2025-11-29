import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

load_dotenv() # Load .env file

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50) 
        page = await browser.new_page()
        await page.goto("https://plaza.newnewnew.space/?692b3b84947b7")
        await page.screenshot(path="example.png")
      


        #Clicking on the Login Button
        await page.get_by_text("Inloggen").first.click()
        #Wait 30 sec
        await page.wait_for_timeout(5000)
        #Fill in username
        await page.fill("input[name='username']", EMAIL)

asyncio.run(main())