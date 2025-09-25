import pytest
from playwright.sync_api import sync_playwright

# first test case to verify google title


def test_google_title(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    assert page.title() == "Google"
    page.wait_for_timeout(3000)
    browser.close()


def test_orangehrm_title(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == "OrangeHRM"
    page.wait_for_timeout(3000)
    browser.close()
