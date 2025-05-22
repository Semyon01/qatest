from playwright.sync_api import Page, expect
from components.base_components import BaseComponent
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page,identifier: str):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input','title_input')
        self.estimated_time_input = Input(page,'create-course-form-estimated-time-input','estimated_time_input')
        self.description_textarea = Textarea(page,'create-course-form-description-input','Textarea')
        self.max_score_input = Input(page,'create-course-form-max-score-input','max_score_input')
        self.min_score_input = Input(page,'create-course-form-min-score-input','min_score_input')

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.title_input).to_be_visible()
        expect(self.title_input).to_have_value(title)

        expect(self.estimated_time_input).to_be_visible()
        expect(self.estimated_time_input).to_have_value(estimated_time)

        expect(self.description_textarea).to_be_visible()
        expect(self.description_textarea).to_have_value(description)

        expect(self.max_score_input).to_be_visible()
        expect(self.max_score_input).to_have_value(max_score)

        expect(self.min_score_input).to_be_visible()
        expect(self.min_score_input).to_have_value(min_score)

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        expect(self.title_input).to_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        expect(self.estimated_time_input).to_have_value(estimated_time)

        self.description_textarea.fill(description)
        expect(self.description_textarea).to_have_value(description)

        self.max_score_input.fill(max_score)
        expect(self.max_score_input).to_have_value(max_score)

        self.min_score_input.fill(min_score)
        expect(self.min_score_input).to_have_value(min_score)
