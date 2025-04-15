from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
        email_input.fill('user.name@gmail.com')

        username_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
        username_input.fill('user.name@gmail.com')

        password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
        password_input.fill('password')

        button_login = page.locator('//button[@data-testid="registration-page-registration-button"]')
        button_login.click()

        allert = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')

        expect(allert).to_have_text('Dashboard')

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_header = page.locator('//h6[@data-testid="courses-list-toolbar-title-text"]')
        expect(courses_header).to_have_text('Courses')

        icon = page.locator('[data-testid="courses-list-empty-view-icon"]')
        expect(icon).to_be_visible()

        text_1 = page.locator('[data-testid="courses-list-empty-view-title-text"]')
        expect(text_1).to_have_text('There is no results')

        text_2 = page.locator('[data-testid="courses-list-empty-view-description-text"]')
        expect(text_2).to_have_text('Results from the load test pipeline will be displayed here')