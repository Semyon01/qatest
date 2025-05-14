from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_components import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,f'{identifier}-drawer-list-item-icon','icon')
        self.title = Text(page,f'{identifier}-drawer-list-item-title-text','text')
        self.button = Button(page,f'{identifier}-drawer-list-item-button','button')

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)