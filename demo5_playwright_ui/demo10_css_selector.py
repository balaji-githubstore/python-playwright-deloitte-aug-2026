from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://orangehrm.com/book-a-free-demo")

    # page.locator("xpath=//button[text()='Allow all']").click()

    # page.locator("text=Allow all").click()

    page.locator("button:has-text('Allow all')").click()

    # page.locator("button",has_text='Allow all').click()

    page.locator("css=#Form_getForm_FullName").fill("John Wick")
    page.locator("css=#Form_getForm_Email").fill("john@gmail.com")
    # dropdown with select tag
    page.locator("css=select[name='Country']").select_option(label="India")


    page.wait_for_timeout(5000)
    browser.close()
