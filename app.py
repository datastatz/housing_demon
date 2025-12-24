import asyncio
from playwright.async_api import async_playwright
import requests



def send_mobile_notification(title, message):
    """Stuur een mobiele notificatie via ntfy.sh"""
    requests.post(
        "https://ntfy.sh/mijn-housing-alerts",  # Kies je eigen topic naam
        data=message.encode('utf-8'),
        headers={
            "Title": title.encode('utf-8'),  # Encode title als UTF-8
            "Tags": "house"  # Voegt een huisje emoji toe in ntfy
        }
    )

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) 
        page = await browser.new_page()
        await page.goto("https://www.roofz.eu/availability", timeout=60000, wait_until="domcontentloaded")
        
      

 
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

        #Selecteer Filter
        await page.locator(".filter-bar__trigger").click()
        await page.wait_for_timeout(5000) 

        # Open de Location dropdown (die "All locations" toont)
        await page.locator(".select-control.no-label").filter(has_text="All locations").click()
        await page.wait_for_timeout(5000)

        # Nu Amsterdam selecteren
        await page.locator("li[value='Amsterdam']").click()
        await page.wait_for_timeout(5000)

        # Klik op close button
        await page.locator(".close-btn").click()
        await page.wait_for_timeout(5000)

        # Haal alle property titles op
        titles_elements = await page.locator(".property__title").all()
        
        # Maak lijst van huidige titles
        titles = []
        for title in titles_elements:
            text = await title.text_content()
            titles.append(text.strip())

        # Print elke titel
        print("=== Property Titles ===")
        for title in titles:
            print(title)
        print(f"=== Totaal: {len(titles)} properties ===")

        # Oude titles (bekende waarden)
        oldTitles = [
            "Nieuwe Osdorpergracht 410 B",
            "Schipluidenlaan 506",
            "Panamalaan 427",
            "Jan van Galenstraat 472",
            "Jan van Galenstraat 488",
            "Jan van Galenstraat 448",
            "Spaklerweg 14 H-25",
            "Spaklerweg 14 H-18",
            "Spaklerweg 14 D-7",
            "Spaklerweg 14 D-20",
            "Jan van Galenstraat 500",
            "Nieuwe Osdorpergracht 412 E",
            "Nieuwe Osdorpergracht 374 K",
            "Spaklerweg 14 D-21",
            "Schipluidenlaan 912",
            "Schipluidenlaan 636",
            "Panamalaan 431",
            "Schipluidenlaan 906",
            "Panamalaan 413",
            "Panamalaan 277",
            "Nieuwe Osdorpergracht 422 A",
            
        ]

        # Vergelijk titles
        print("\n=== Vergelijking ===")
        
        # Nieuwe titles (in titles maar niet in oldTitles)
        new_titles = [t for t in titles if t not in oldTitles]
        if new_titles:
            print(f"🆕 NIEUWE PROPERTIES ({len(new_titles)}):")
            for t in new_titles:
                print(f"  - {t}")
            
            # Stuur mobiele notificatie
            send_mobile_notification(
                "Nieuwe Woning Gevonden!",
                "\n".join(new_titles)
            )
        else:
            print("Geen nieuwe properties gevonden.")

        # Verwijderde titles (in oldTitles maar niet in titles)
        removed_titles = [t for t in oldTitles if t not in titles]
        if removed_titles:
            print(f"❌ VERWIJDERDE PROPERTIES ({len(removed_titles)}):")
            for t in removed_titles:
                print(f"  - {t}")

        # Check of ze exact gelijk zijn
        if set(titles) == set(oldTitles):
            print("✅ Titles zijn identiek!")
        else:
            print(f"⚠️  Titles zijn NIET identiek")
            print(f"   Oud: {len(oldTitles)} | Nieuw: {len(titles)}")


asyncio.run(main())