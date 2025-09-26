# Copilot Instructions for uitesting

## Project Overview
This repository is for browser automation and UI testing using Playwright and pytest in Python. It includes both synchronous and asynchronous Playwright usage, with a focus on parameterized, maintainable, and readable test cases for web forms and login flows.

## Key Components
- `tests/`: Contains pytest-based test suites. Example: `test_registration_form.py` for form automation and validation, `test_automation.py` for Google and OrangeHRM tests.
- `requirements.txt`: Lists all required Python packages, including Playwright, pytest, and plugins for HTML reporting and parallelization.
- Standalone scripts (`excercise.py`, `first_test_sync.py`, `first_test_aysnc.py`, `locators.py`): Demonstrate Playwright usage patterns, selectors, and browser control.

## Test Patterns & Conventions
- **Fixtures**: Use `browser` (session/module scope) and `page` (function scope) fixtures for Playwright setup/teardown.
- **Parameterized Tests**: Use `@pytest.mark.parametrize` for data-driven testing (see `test_registration_form.py`).
- **Selectors**: Prefer Playwright's `locator`, `get_by_role`, and `get_by_text` for robust element selection. Use explicit waits (`wait_for_selector`) for dynamic elements.
- **Form Automation**: Use helper functions (e.g., `fill_registration_form`) to encapsulate multi-step flows.
- **Modal/Result Validation**: Use Playwright's `expect` assertions to validate UI state and submitted data.
- **Headless/Headful**: Default to `headless=False` for debugging; set `headless=True` for CI or speed.

## Developer Workflows
- **Install dependencies**: `pip install -r requirements.txt`
- **Install browsers**: `python -m playwright install`
- **Run all tests**: `pytest`
- **Run a specific test file**: `pytest tests/test_registration_form.py`
- **Generate HTML report**: `pytest --html=reports/report.html`
- **Run tests in parallel**: `pytest -n auto`

## Project-Specific Notes
- **No Page Object Model (POM)**: Tests are currently function-based for clarity. If adding POM, place page classes in a `pages/` directory.
- **Async and Sync**: Both sync (`playwright.sync_api`) and async (`playwright.async_api`) styles are demonstrated. Do not mix in the same test.
- **Selector Examples**: See `locators.py` and `excercise.py` for CSS/XPath usage and Playwright best practices.
- **Test Data**: Parameterized data is defined inline in test files for clarity.

## External Integrations
- No external services or APIs are integrated. All tests run against public demo sites.

## Example: Running a Registration Form Test
```sh
pytest tests/test_registration_form.py --html=reports/report.html
```

## Key Files
- `tests/test_registration_form.py`: Full-featured, parameterized Playwright+pytest test for demoqa.com registration form.
- `tests/test_automation.py`: Google and OrangeHRM title/login tests with parameterization.
- `requirements.txt`: All dependencies for local and CI runs.

---
If any conventions or workflows are unclear, please provide feedback so this document can be improved.
