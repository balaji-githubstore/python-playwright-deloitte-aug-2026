from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://www.salesforce.com/in/sales/free-trial/ee/")

    """
    2. Enter first name as “John”
    3. Enter last name as “wick”
    5. Select Employees as “201-500 employees"
    8. Do not fill the phone number
    9. Click on check box
    10. Click on start my free trial
    11. Get the error message displayed “Enter a valid phone number" 
    """

    # enter firstname as john - use xpath and try
    page.locator("css=input[name='firstName']").fill("john")

    page.locator("css=input[name='lastName']").fill("wick")

    page.locator("css=select[name='employees']").select_option(label="201-500 employees")

    page.locator("css=div[class='checkbox--faux']").click()

    page.locator("css=button[aria-label='Start my free trial: Sales']").click()

    # page.locator("span:has-text('Start my free trial')").click()
    
    actual_error=page.locator("div[class*='wes:text-red wes:transition-colors']").and_(page.locator("div:has-text('Enter valid phone number.')")).inner_text()
    print(actual_error)

    actual_error=page.locator("div:has-text('Enter valid phone number.')").nth(12).inner_text()
    print(actual_error)

    page.wait_for_timeout(5000)
    browser.close()
