from operator import index

import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state: Page, create_course_page: CreateCoursePage,courses_list_page: CoursesListPage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.toolbar_view.check_visible_create_course_title()
    create_course_page.toolbar_view.check_visible(is_create_course_disabled=True)
    create_course_page.exercises_empty_view.check_visible()
    create_course_page.image_upload_widget.check_visible()
    create_course_page.create_course_form.fill_create_course_form(title = '',description ='',estimated_time ='',max_score= '0',min_score = '0')
    create_course_page.create_exercise_form.check_visible(index=0,title='',description='')
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file='C:\\Users\\s.a.esmenov\\PycharmProjects\\qatest\\test_data\\files\\image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10"
    )
    create_course_page.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.courses_view.check_visible(index=0,title='Playwright',min_score='10',max_score='100',estimated_time='2 weeks')


