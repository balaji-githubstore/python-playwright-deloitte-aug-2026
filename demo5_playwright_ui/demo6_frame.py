from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("file:///D:/Mine/Components/Demo/demo1.html")


    page.locator("xpath=//input[@id='fname']").fill("wick")


    signup_frame=page.frame_locator("xpath=//iframe[contains(@src,'demo3')]")
    signup_frame.locator("xpath=//button[text()='Sign up with google']").click()


    login_frame=page.frame_locator("xpath=//iframe[contains(@src,'demo2')]")
    login_frame.locator("xpath=//button[text()='Login with Google']").click()
    

    time.sleep(5)
    browser.close()