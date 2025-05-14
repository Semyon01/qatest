from components.base_components import BaseComponent

from playwright.sync_api import Page, expect

from elements.input import Input


class  RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.username_input = Input(page,'registration-form-username-input', 'username')
        self.password_input =  Input(page,'registration-form-password-input','password')

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)
