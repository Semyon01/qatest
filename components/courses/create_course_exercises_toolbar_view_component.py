from playwright.sync_api import Page, expect
from components.base_components import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page,identifier: str):
        super().__init__(page)

        self.title = Text(page,'create-course-exercises-box-toolbar-title-text', 'title')
        self.create_exercise_button = Button(page,
            'create-course-exercises-box-toolbar-create-exercise-button','Button'
        )

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')

        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()