from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context(viewport={"width": 1536, "height": 816})
    page = context.new_page()

    page.goto("https://www.ilovepdf.com/pdf_to_word")

    # option 2 - page.expect_filechooser()
    with page.expect_file_chooser() as file_chooser_info:
        page.locator("xpath=//span[text()='Select PDF file']").click()
    file_chooser=file_chooser_info.value

    file_chooser.set_files(r"D:\Mine\Balaji Dinakaran Trainer Profile AI 2026.pdf")

    time.sleep(5)
    browser.close()
    