import pytest
from playwright.sync_api import expect, Page

from pages.dashboard_page import DashboardPage


def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.sidebar.check_visible()



