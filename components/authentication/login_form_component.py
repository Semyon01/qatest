from components.base_components import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page,'login-form-password-input', 'password')

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)