from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Open Browser and launch it
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # enter the target url
    page.goto("https://demo.automationtesting.in/Index.html")

    # CSS Selector
    # by id #, by class .

    emailtextbox = page.wait_for_selector('#email')
    emailtextbox.fill("test123@email.com")

    button = page.wait_for_selector('#enterimg')
    button.click()

    print(page.title())

    # Wait for 3 second before closing the browser
    page.wait_for_timeout(3000)

    browser.close()
