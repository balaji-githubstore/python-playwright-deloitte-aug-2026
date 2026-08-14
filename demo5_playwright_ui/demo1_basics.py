from playwright.sync_api import sync_playwright

# playwright instance 
with sync_playwright() as playwright:
    # browser instance 
    browser= playwright.chromium.launch(channel="chrome",headless=False)

    # browser context 
    context=browser.new_context()

    # new tab - page 
    page=context.new_page()

    page.goto("https://www.google.com/")

    actual_title=page.title()
    print(actual_title)





