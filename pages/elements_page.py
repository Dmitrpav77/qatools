import time

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators
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