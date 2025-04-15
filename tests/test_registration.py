
from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
        email_input.fill('user.name@gmail.com')

        username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
        username_input.fill('user.name@gmail.com')

        password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
        password_input.fill('password')

        button_login = page.locator('//button[@data-testid="registration-page-registration-button"]')
        button_login.click()

        allert = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')

        expect(allert).to_have_text('Dashboard')

        page.wait_for_timeout(5000)