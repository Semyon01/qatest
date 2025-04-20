import os

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, Browser

@pytest.fixture
def chromium_page(playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield  browser.new_page()

@pytest.fixture(scope="session")
def  initialize_browser_state(browser: Browser) -> None:
        if not os.path.exists("browser-state.json"):
                # Создаем новый контекст и страницу
                context = browser.new_context()
                chromium_page = context.new_page()
                chromium_page.goto(
                        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

                email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
                email_input.fill('user.name@gmail.com')

                username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
                username_input.fill('username')

                password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
                password_input.fill('password')

                registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
                registration_button.click()
                context.storage_state(path="browser-state.json")

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page