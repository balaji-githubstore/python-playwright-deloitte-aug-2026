from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://orangehrm.com/")

    # check for element present 
    if page.locator("xpath=//button[text()='Allow all']").count()>0:
            page.locator("xpath=//button[text()='Allow all']").click()

    # will expect a new popup (new tab)
    with page.expect_popup() as popup_info:

        # click on element that opens new tab (popup)
        page.locator("xpath=//a[normalize-space()='AI Help Desk']").click()

    # get the new tab (Page) detail from expect_popup method 
    new_page=popup_info.value

    new_page.locator("xpath=//input[@id='chat-input']").fill("hello")

    # click on send 
    # print title from both the tab 
    print(page.title())
    print(new_page.title())
    time.sleep(5)
    browser.close()

   