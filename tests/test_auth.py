from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_auth():
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        page = chromium.new_page()

        page.goto(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

        email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input.fill('user.name@gmail.com')

        password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill('1234')

        button_login = page.locator('//button[@data-testid="login-page-login-button"]')
        button_login.click()

        allert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')

        expect(allert).to_be_visible()
        expect(allert).to_have_text('Wrong email or password')

        page.wait_for_timeout(5000)
