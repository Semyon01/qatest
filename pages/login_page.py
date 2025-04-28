from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        self.password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        self.button_login = page.locator('//button[@data-testid="login-page-login-button"]')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.allert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    def fill_login_form(self, email, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)


    def click_login_button(self):
        self.button_login.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visibale_allert(self):
        expect(self.allert).to_be_visible()
        expect(self.allert).to_have_text('Wrong email or password')
