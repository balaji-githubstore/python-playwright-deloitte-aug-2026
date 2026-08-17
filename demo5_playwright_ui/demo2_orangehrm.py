from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://orangehrm.com/book-a-free-demo")

    page.locator("xpath=//button[text()='Allow all']").click()

    page.locator("xpath=//input[@id='Form_getForm_FullName']").fill("John Wick")
    page.locator("xpath=//input[@id='Form_getForm_Email']").fill("john@gmail.com")
    # dropdown with select tag
    page.locator("xpath=//select[@id='Form_getForm_Country']").select_option(label="India")

    # enter company name as deloitte 
    page.locator("xpath=//input[@id='Form_getForm_CompanyName']").fill("Deloitte")
    # enter job title as QA lead 
    page.locator("xpath=//input[@id='Form_getForm_JobTitle']").fill("QA lead")
    # select employee count - >1000 
    page.locator("xpath=//select[@id='Form_getForm_NoOfEmployees']").select_option(label="> 1,000")

    page.locator("xpath=//input[@id='Form_getForm_action_submitForm']").click()
    time.sleep(5)

    browser.close()


