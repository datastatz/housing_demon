
Add to Chat⌘L
cursor agent to run Agent • ⌘K to generate command
help me in hele kleine code snippet, echt heel klein voor een vermoeide junior dev

Minimale Playwright Snippet 🐣
Kopieer dit naar je app.py:
from playwright.sync_api import sync_playwrightdef run():    with sync_playwright() as p:        # Start browser (headless=False zodat je ziet wat er gebeurt)        browser = p.chromium.launch(headless=False)        page = browser.new_page()                # 1. Ga naar website        page.goto("https://example.com/login")                # 2. Vul login in        page.fill("#username", "jouw_username")        page.fill("#password", "jouw_password")        page.click("#login-button")                # 3. Wacht even en ga naar andere pagina        page.wait_for_timeout(2000)  # 2 seconden        page.goto("https://example.com/andere-pagina")                # 4. Klik op iets        page.click("button.reageer")                # Klaar!        browser.close()# Run hetrun()
🧪 Test het
# In je terminal (met venv actief)python app.py
🔍 Hoe vind je die selectors (#username, button.reageer)?
Open de website in Chrome
Rechtermuisklik op het element → Inspect
Kijk naar de HTML en gebruik:
#id voor id's
.class voor classes
button voor tags
Dat is alles! Pas de URL's en selectors aan voor jouw website. Werkt het? Dan voegen we daarna de scheduler toe. 🙂
import re

from playwright.sync_api import Page, expect



def test_has_title(page: Page):

    page.goto("https://playwright.dev/")



    # Expect a title "to contain" a substring.

    expect(page).to_have_title(re.compile("Playwright"))



def test_get_started_link(page: Page):

    page.goto("https://playwright.dev/")



    # Click the get started link.

    page.get_by_role("link", name="Get started").click()



    # Expects page to have a heading with the name of Installation.

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()



ik vond dit in hun docs is dit een goed startpunt?

Goed gevonden, maar... 🤔
Wat je daar hebt gevonden is de test-versie van Playwright (voor pytest). Dat is bedoeld om websites te testen, niet om een script te draaien.
Verschil:
Test versie (jouw snippet)	Script versie (wat jij nodig hebt)
def test_has_title(page):	with sync_playwright() as p:
Draait via pytest	Draait via python app.py
Voor website testen	Voor automation/scraping
page wordt automatisch gegeven	Je maakt zelf page aan
Jouw versie zou zijn:
from playwright.sync_api import sync_playwrightdef run():    with sync_playwright() as p:        browser = p.chromium.launch(headless=False)        page = browser.new_page()                # Ga naar website        page.goto("https://playwright.dev/")                # Klik op "Get started" link        page.get_by_role("link", name="Get started").click()                # Wacht 3 sec zodat je het ziet        page.wait_for_timeout(3000)                browser.close()run()
Wat WEL handig is uit die docs:
De selectors zijn super handig! Deze zijn beter dan CSS selectors:
# Beter (wat je in de docs zag):page.get_by_role("link", name="Get started").click()page.get_by_role("button", name="Login").click()page.get_by_label("Username").fill("jan")page.get_by_placeholder("Enter email").fill("test@test.com")# Minder goed (mijn eerdere voorbeeld):page.click("#login-button")page.fill("#username", "jan")
De get_by_role, get_by_label methodes zijn robuuster en breken minder snel als de website verandert.
TL;DR
Gebruik mijn structuur (with sync_playwright()) maar steel de selector-methodes (get_by_role, get_by_label) uit de docs! 👍
oke even weer naar de basis, ik vind het fijn om met officieele docs te leren kun je me begeleiden naar de site waar ik officiele docs kan zien en ze ook kan nabootsen?

Officiële Playwright Python Docs 📚
De juiste startpagina voor jou:
👉 https://playwright.dev/python/docs/library
Dit is de "Library" sectie - precies wat jij nodig hebt voor automation scripts!
⚠️ Let op in de docs:
De Playwright docs hebben twee secties:
Sectie	URL	Voor jou?
Library	/python/docs/library	✅ JA - voor scripts
Test (pytest)	/python/docs/intro	❌ NEE - voor testen
Zorg dat je in de Library sectie zit!
📖 Handige pagina's om te lezen (in volgorde):
Getting Started
https://playwright.dev/python/docs/library
Locators (hoe je elementen vindt)
https://playwright.dev/python/docs/locators
Actions (klikken, typen, etc.)
https://playwright.dev/python/docs/input
Auto-waiting (Playwright wacht automatisch)
https://playwright.dev/python/docs/actionability