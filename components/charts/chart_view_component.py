from playwright.sync_api import Page, expect
from components.base_components import BaseComponent

class ChartViewComponent (BaseComponent):
    def __init__(self, page: Page,identifier: str, chart_type: str):
        super().__init__(page)

        self.students_title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.students_chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

        self.activities_title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.activities_chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

        self.courses_title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.courses_chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

        self.scores_title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.scores_chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible_students_chart(self):
        expect(self.students_title).to_be_visible()
        expect(self.students_title).to_have_text('Students')
        expect(self.students_chart).to_be_visible()

    def check_visible_activities_chart(self):
        expect(self.activities_title).to_be_visible()
        expect(self.activities_title).to_have_text('Activities')
        expect(self.activities_chart).to_be_visible()

    def check_visible_courses_chart(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')
        expect(self.courses_chart).to_be_visible()

    def check_visible_scores_chart(self):
        expect(self.scores_title).to_be_visible()
        expect(self.scores_title).to_have_text('Scores')
        expect(self.scores_chart).to_be_visible()
