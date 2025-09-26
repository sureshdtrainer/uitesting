import pytest
from playwright.sync_api import sync_playwright, Page, expect

# Test data for parameterization
registration_test_data = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "gender": "Male",
        "mobile": "1234567890",
        "dob": {"day": "10", "month": "May", "year": "1990"},
        "subjects": ["Maths", "Physics"],
        "hobbies": ["Sports", "Reading"],
        "address": "123 Main St, Cityville",
        "state": "NCR",
        "city": "Delhi"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "gender": "Female",
        "mobile": "9876543210",
        "dob": {"day": "20", "month": "August", "year": "1995"},
        "subjects": ["English"],
        "hobbies": ["Music"],
        "address": "456 Side Rd, Townsville",
        "state": "Uttar Pradesh",
        "city": "Agra"
    }
]


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def fill_registration_form(page: Page, data: dict):
    # Remove ad overlays and banners that block clicks
    page.evaluate("""
        for (const sel of ['#fixedban', '.modal-backdrop', '.adsbygoogle', 'iframe[title*=\"ad\"], iframe[src*=\"ads\"]']) {
            document.querySelectorAll(sel).forEach(e => e.remove());
        }
    """)
    page.goto("https://demoqa.com/automation-practice-form")
    # Close modal if present from previous test
    if page.locator('#closeLargeModal').is_visible():
        page.click('#closeLargeModal')
        expect(page.locator('#example-modal-sizes-title-lg')
               ).not_to_be_visible()
    page.fill("#firstName", data["first_name"])
    page.fill("#lastName", data["last_name"])
    page.fill("#userEmail", data["email"])
    # Gender radio button: click the label by index (Male=0, Female=1, Other=2)
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    idx = gender_map.get(data["gender"], 0)
    page.locator('label[for^="gender-radio-"]').nth(idx).click()
    page.fill("#userNumber", data["mobile"])
    # Date of Birth
    page.click("#dateOfBirthInput")
    page.select_option(".react-datepicker__month-select", data["dob"]["month"])
    page.select_option(".react-datepicker__year-select", data["dob"]["year"])
    page.click(f'.react-datepicker__day--0{int(data["dob"]["day"]):02d}')
    # Subjects
    for subject in data["subjects"]:
        page.fill("#subjectsInput", subject)
        page.keyboard.press("Enter")
        # Hobbies (use input id)
        hobby_ids = {
            "Sports": "hobbies-checkbox-1",
            "Reading": "hobbies-checkbox-2",
            "Music": "hobbies-checkbox-3"
        }
        for hobby in data["hobbies"]:
            page.check(f'#{hobby_ids[hobby]}')
    page.fill("#currentAddress", data["address"])
    # State and City
    # State and City (type and enter)
    page.click("#state")
    page.keyboard.type(data["state"])
    page.keyboard.press("Enter")
    page.click("#city")
    page.keyboard.type(data["city"])
    page.keyboard.press("Enter")
    # Submit
    page.click("#submit")


@pytest.mark.parametrize("data", registration_test_data)
def test_registration_form(page, data):
    fill_registration_form(page, data)
    # Assert modal appears
    expect(page.locator("#example-modal-sizes-title-lg")).to_be_visible()
    # Assert submitted data in modal
    modal = page.locator(".modal-content")
    expect(modal).to_contain_text(data["first_name"])
    expect(modal).to_contain_text(data["last_name"])
    expect(modal).to_contain_text(data["email"])
    expect(modal).to_contain_text(data["gender"])
    expect(modal).to_contain_text(data["mobile"])
    expect(modal).to_contain_text(data["dob"]["year"])
    for subject in data["subjects"]:
        expect(modal).to_contain_text(subject)
    for hobby in data["hobbies"]:
        expect(modal).to_contain_text(hobby)
    expect(modal).to_contain_text(data["address"])
    expect(modal).to_contain_text(data["state"])
    expect(modal).to_contain_text(data["city"])
    # Close modal
    page.click("#closeLargeModal")
    expect(page.locator("#example-modal-sizes-title-lg")).not_to_be_visible()
