from playwright.sync_api import sync_playwright, Page
import os
from datetime import datetime


# playwright instance
with sync_playwright() as playwright:
    # browser instance
    browser = playwright.chromium.launch(channel="chrome", headless=False)

    # browser context
    context = browser.new_context()

    # new tab - page
    page: Page = context.new_page()

    page.goto("https://www.google.com/")

    actual_title: str = page.title()
    print(actual_title)

    page.screenshot(path="error.png")

    print(datetime.now())

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    page.screenshot(
        path=f"screenshots/sc_{timestamp}.png"
    )


import logging

logger=logging.getLogger()

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger.info('Started')

logger.info('Finished')
