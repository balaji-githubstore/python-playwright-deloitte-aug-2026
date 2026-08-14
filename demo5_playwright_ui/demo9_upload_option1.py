from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width": 1536, "height": 816})
    page = context.new_page()

    page.goto("https://www.ilovepdf.com/pdf_to_word")

    # option 1 -- check for //input[@type='file']
    page.locator("xpath=//input[@type='file']").set_input_files(r"D:\Mine\Balaji Dinakaran Trainer Profile AI 2026.pdf")

    time.sleep(5)
    browser.close()
