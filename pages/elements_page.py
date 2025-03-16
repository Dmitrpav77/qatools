import random
from selenium.webdriver.common.by import By
import time
from time import process_time

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person = next(generated_person())
        input_full_name = person.full_name
        input_email = person.email
        input_current_address = person.current_address
        input_permanent_address = person.permanent_address
        self.element_is_visible(self.locators.INPUT_FULL_NAME).send_keys(input_full_name)
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(input_email)
        self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS).send_keys(input_current_address)
        self.element_is_visible(self.locators.INPUT_PERMANENT_ADDRESS).send_keys(input_permanent_address)
        self.go_to_element(self.element_is_clickable(self.locators.SUBMIT))
        self.element_is_clickable(self.locators.SUBMIT).click()
        return input_full_name, input_email, input_current_address, input_permanent_address

    def get_output_fields_text(self):
        output_full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text
        output_email = self.element_is_present(self.locators.OUTPUT_EMAIL).text
        output_current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text
        output_permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text
        return output_full_name.split(":")[1], output_email.split(":")[1], output_current_address.split(":")[1], output_permanent_address.split(":")[1]

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def expand_all(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def random_click_checkbox(self):
        checkbox_list = self.elements_are_visible(self.locators.CHECKBOX_LIST)
        for i in range(30):
            self.go_to_element(checkbox_list[random.randint(0, 16)])
            checkbox_list[random.randint(0, 16)].click()


    def get_title_selected_checkboxes(self):
        selected_checkboxes = self.elements_are_present(self.locators.CHECKED_ITEMS)
        title_list = []
        for i in selected_checkboxes:
            item = i.find_element(by=By.XPATH, value='.//ancestor::span[@class="rct-text"]')
            title_list.append(item.text.lower().replace(" ", "").replace(".doc", ""))
        return title_list

    def get_title_output_checkboxes(self):
        title_checkboxes = self.elements_are_present(self.locators.OUTPUT_SELECTED_CHECKBOXES)
        title_list = []
        for i in title_checkboxes:
            title_list.append(i.text.lower().replace(" ", "").replace(".doc", ""))
        return title_list


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def random_radiobutton_click(self, choice):
        choices = {"Yes":self.locators.YES_BUTTON,
                   "Impressive":self.locators.IMPRESSIVE_BUTTON,
                   "No":self.locators.NO_BUTTON}
        self.element_is_visible(choices[choice]).click()
        return choice

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


