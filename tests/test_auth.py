import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.authorization

@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),  # Невалидные email и password
        ("user.name@gmail.com", "  "),       # Невалидный email и пустой password (два пробела)
        ("  ", "password"),                  # Пустой email (два пробела) и невалидный password
    ],
)
def test_wrong_email_or_password_auth(chromium_page: Page, email: str, password: str):


        chromium_page.goto(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

        email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input.fill(email)

        password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill(password)

        button_login = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
        button_login.click()

        allert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

        expect(allert).to_be_visible()
        expect(allert).to_have_text('Wrong email or password')

        chromium_page.wait_for_timeout(5000)
