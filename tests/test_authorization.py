import pytest
from playwright.sync_api import sync_playwright, expect, Page
from pages.login_page import LoginPage

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
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.login_form.fill_login_form(email=email, password=password)
    login_page.login_form.click_login_button()
    login_page.login_form.check_visibale_allert()
