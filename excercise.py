from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Open Browser and launch it
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # enter the target url
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # CSS Selector with attribute
    page.wait_for_selector('input[name="username"]').fill("Admin")
    page.wait_for_selector('input[type="password"]').fill("admin123")
    page.wait_for_selector('button[type="submit"]').click()

    print(page.title())

    # Wait for 3 second before closing the browser
    page.wait_for_timeout(3000)

    browser.close()
