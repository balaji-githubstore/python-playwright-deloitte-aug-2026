from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width": 1536, "height": 816})
    page = context.new_page()

    page.goto("https://www.nasscom.in/nasscom-membership")

    # override the default feature of dialog
    page.on("dialog",lambda dialog:(
        print(dialog.message),
        dialog.accept()
        ))  
    
    # click on caculate fees
    page.locator("xpath=//a[@id='calculate-fee']").click()

    time.sleep(5)
    browser.close()
