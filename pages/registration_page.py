from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class  RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator('//div[@data-testid="registration-form-email-input"]//input')
        self.username_input = page.locator('//div[@data-testid="registration-form-username-input"]//input')
        self.password_input = page.locator('//div[@data-testid="registration-form-password-input"]//input')
        self.login_button = page.locator('//button[@data-testid="registration-page-registration-button"]')




    def fill_registration_form(self, email, password, username: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)


    def click_login_button(self):
        self.login_button.click()


