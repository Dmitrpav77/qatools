import random
import time
from itertools import count

from selenium.webdriver.common.keys import Keys
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


    def check_autocomplete_multiple_colors(self, num):
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Violet", "Indigo", "Magenta", "Aqua"]
        count = 0
        while num != 0:
            self.element_is_visible(self.locators.MULTI_INPUT).send_keys(colors.pop(random.randint(0, len(colors)-1)))
            self.element_is_visible(self.locators.MULTI_INPUT).send_keys(Keys.RETURN)
            num -= 1
            count += 1
        return count


    def check_autocomplete_single_color(self):
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Violet", "Indigo", "Magenta", "Aqua"]
        selected_color = colors.pop(random.randint(0, len(colors)-1))
        self.element_is_visible(self.locators.INPUT_SINGLE_COLOR).click()
        self.element_is_visible(self.locators.INPUT_SINGLE_COLOR).send_keys(selected_color)
        self.element_is_visible(self.locators.INPUT_SINGLE_COLOR).send_keys(Keys.ENTER)
        return selected_color


    def check_selected_single_color_text(self):
        return self.element_is_present(self.locators.OUTPUT_SINGLE_COLOR_TEXT).text

    def count_multi_input(self):
        amount = self.elements_are_present(self.locators.MULTI_INPUT_AMOUNT)
        return len(amount)


