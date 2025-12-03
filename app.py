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
        await page.goto("https://www.roofz.eu/availability")
        await page.screenshot(path="example.png")
      

 
        #Clicking on the Login Button
        await page.get_by_text("WEIGEREN").first.click() # WORKS

        #Wait 
        await page.wait_for_timeout(2000)
        
        #Open de dropdown
        await page.locator(".select-control__select").filter(has_text="Newest").click()
        await page.wait_for_timeout(500)
       
        #Selecteer "Newest"
        await page.locator("li[value='publish-high']").click()

        await page.wait_for_timeout(5000)


asyncio.run(main())