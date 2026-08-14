"""
# 1. Navigate to https://www.online.citibank.co.in/
# 2. Close any pop-up that comes
# 3. Click on My Account
# 4. Click on Banking with Citi
# 5. Enter userid as john123
# 6. Click on Login
# 7. Verify - Enter a valid password

"""
from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://www.online.citibank.co.in/")
    # click on Accept all 
    page.locator("xpath=//button[@id='onetrust-accept-btn-handler']").click()

    page.locator("xpath=//div[text()='My Account']").hover()

    # Click on Banking with Citi that open new tab
    with page.expect_popup() as popup_info:
        page.locator("xpath=//div[text()='Banking with Citi']").click()
    new_page=popup_info.value

    new_page.locator("xpath=//input[@formcontrolname='username']").fill("john")
    new_page.locator("xpath=//button[@id='signInBtn']").click()

    actual_error=new_page.locator("xpath=//span[contains(text(),'valid password')]").inner_text()
    print(actual_error)


    time.sleep(5)
    browser.close()
