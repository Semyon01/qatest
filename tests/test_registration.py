import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):


        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = chromium_page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
        email_input.fill('user.name@gmail.com')

        username_input = chromium_page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
        username_input.fill('user.name@gmail.com')

        password_input = chromium_page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
        password_input.fill('password')

        button_login = chromium_page.locator('//button[@data-testid="registration-page-registration-button"]')
        button_login.click()

        allert = chromium_page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')

        expect(allert).to_have_text('Dashboard')

        chromium_page.wait_for_timeout(5000)