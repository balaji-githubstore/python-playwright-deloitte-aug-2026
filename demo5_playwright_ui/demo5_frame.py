from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://app.thetestingacademy.com/playwright/frames/")


    vehicle_frame_section= page.frame_locator("xpath=//iframe[@name='vehicle-form']")

    # enter Vehicle name as creta 
    vehicle_frame_section.locator("xpath=//input[@name='vehicleName']").fill("creta")

    vehicle_frame_section.locator("xpath=//input[@name='regNumber']").fill("76876")

    # select vehicle type as SUV

    # year as 2020

    # enter notes as - for resale

    # submit registration 

    time.sleep(5)
    browser.close()