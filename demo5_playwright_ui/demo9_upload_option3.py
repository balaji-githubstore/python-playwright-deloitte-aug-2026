from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width": 1536, "height": 816})
    page = context.new_page()

    page.goto("https://www.ilovepdf.com/pdf_to_word")

    # option 3 - page.on(“filechooser”) - registering the event that runs when filechooser comes into picture
    page.on("filechooser",lambda filechooser:filechooser.set_files(r"D:\Mine\Balaji Dinakaran Trainer Profile AI 2026.pdf"))    

    # click on element that opens filechooser
    page.locator("xpath=//span[text()='Select PDF file']").click()    
    

    page.wait_for_timeout(10000)
    browser.close()
    