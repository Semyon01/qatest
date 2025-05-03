import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill_registration_form(email='test@mail.com', password='password', username='user')
        registration_page.registration_form.click_login_button()

