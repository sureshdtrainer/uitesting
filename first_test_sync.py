from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Open Browser and launch it
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # enter the target url
    page.goto("https://www.google.com")

    print(page.title())

    # Wait for 3 second before closing the browser
    page.wait_for_timeout(3000)

    browser.close()
