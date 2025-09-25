import pytest
from playwright.sync_api import sync_playwright

# first test case to verify google title


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.wait_for_timeout(3000)
    page.close()


def test_google_title(page):
    page.goto("https://www.google.com")
    assert page.title() == "Google"


def test_orangehrm_title(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == "OrangeHRM"


@pytest.mark.parametrize('username,password', [('testuser1', 'testpwd1'), ('testuser2', 'testpwd2')])
def test_invalid_orangehrm_login(page, username, password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_selector('//input[@name="username"]').fill(username)
    page.wait_for_selector('//input[@placeholder="Password"]').fill(password)
    page.wait_for_selector('//button[@type="submit"]').click()

    page.wait_for_timeout(2000)

    error = page.wait_for_selector('//div[@role="alert"]//p').text_content()
    assert "Invalid credentials" == error
