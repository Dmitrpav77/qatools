import time

from locators.widgets_page_locators import WidgetsPageLocators
from pages.base_page import BasePage


class WidgetsPage(BasePage):
    locators = WidgetsPageLocators()
    def accordian_check(self):
        first_accordian = self.element_is_visible(self.locators.FIRST_ACCORDIAN)
        second_accordian = self.element_is_visible(self.locators.SECOND_ACCORDIAN)
        third_accordian = self.element_is_visible(self.locators.THIRD_ACCORDIAN)
        self.go_to_element(first_accordian)
        time.sleep(1)
        first_accordian_text = self.element_is_present(self.locators.FIRST_ACCORDIAN_TEXT).text
        self.go_to_element(second_accordian)
        self.element_is_visible(self.locators.SECOND_ACCORDIAN).click()
        time.sleep(1)
        second_accordian_text = self.element_is_present(self.locators.SECOND_ACCORDIAN_TEXT).text
        self.go_to_element(third_accordian)
        third_accordian.click()
        time.sleep(1)
        third_accordian_text = self.element_is_present(self.locators.THIRD_ACCORDIAN_TEXT).text
        return len(first_accordian_text), len(second_accordian_text), len(third_accordian_text)