from components.base_components import BaseComponent

from playwright.sync_api import Page, expect


class  RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.email_input = page.get_by_test_id(f'{identifier}-email-input').locator('input')
        self.username_input = page.get_by_test_id(f'{identifier}-username-input').locator('input')
        self.password_input = page.get_by_test_id(f'{identifier}-password-input').locator('input')
        self.login_button = page.get_by_test_id('registration-page-registration-button')




    def fill_registration_form(self, email, password, username: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)


    def click_login_button(self):
        self.login_button.click()
