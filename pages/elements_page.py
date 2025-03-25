import random


import requests
from selenium.webdriver.common.by import By
import time
from time import process_time

from generator.generator import generated_person
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebtablePageLocators, ButtonsPageLocators, LinksPageLocators
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

class WebTablePage(BasePage):
    locators = WebtablePageLocators()

    def add_new_person(self, amount):
        result_person = []
        while amount != 0:
            person = next(generated_person())
            first_name = person.first_name
            last_name = person.last_name
            email = person.email
            age = person.age
            salary = person.salary
            department = person.department
            self.go_to_element(self.element_is_visible(self.locators.ADD_BUTTON))
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.go_to_element(self.element_is_visible(self.locators.SUBMIT))
            self.element_is_visible(self.locators.SUBMIT).click()
            print(first_name)
            amount -= 1
            result_person = [first_name, last_name, str(age), email, str(salary), department]
        return result_person

    def find_person(self, search):
        self.element_is_visible(self.locators.SEARCH_INPUT).click()
        self.element_is_visible(self.locators.SEARCH_INPUT).clear()
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(search)
        table_list = self.elements_are_present(self.locators.ALL_TABLE_ROWS)
        data = []
        for i in table_list:
            data.append(i.text.splitlines())
        return data

    def edit_person(self):
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        person = next(generated_person())
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        age = person.age
        salary = person.salary
        department = person.department
        self.element_is_visible(self.locators.FIRST_NAME).clear()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).clear()
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).clear()
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).clear()
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).clear()
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_search_result(self):
        if self.element_is_present(self.locators.NO_ROWS_FOUND).text == "No rows found":
            return "No rows found"

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def double_click_on_button(self):
        self.double_click(self.element_is_visible(self.locators.DOUBLE_CLICK))
        return self.element_is_present(self.locators.OUTPUT_DOUBLE_CLICK).text

    def right_click_on_button(self):
        self.right_click(self.element_is_visible(self.locators.RIGHT_CLICK))
        return self.element_is_present(self.locators.OUTPUT_RIGHT_CLICK).text

    def dynamic_click_on_button(self):
        self.dynamic_click(self.element_is_visible(self.locators.DYNAMIC_CLICK))
        return self.element_is_present(self.locators.OUTPUT_DYNAMIC_CLICK).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    def open_new_tab_simple_link(self):
        self.go_to_element(self.element_is_visible(self.locators.SIMPLE_LINK))
        self.element_is_visible(self.locators.SIMPLE_LINK).click()
        href_link = self.element_is_present(self.locators.SIMPLE_LINK).get_attribute('href')
        return href_link


    def check_current_url(self):
        return self.driver.current_url


    def open_new_tab_dynamic_link(self):
        self.go_to_element(self.element_is_visible(self.locators.DYNAMIC_LINK))
        self.element_is_visible(self.locators.DYNAMIC_LINK).click()
        href_link = self.element_is_present(self.locators.SIMPLE_LINK).get_attribute('href')
        return href_link


    def open_link_created(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_CREATED)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/created')
        return request.status_code


    def open_link_no_content(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_NO_CONTENT)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/no-content')
        return request.status_code


    def open_link_moved(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_MOVED)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/moved')
        return request.status_code


    def open_link_bad_request(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_BAD_REQUEST)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/bad-request')
        return request.status_code


    def open_link_unauthorized(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_UNAUTHORIZED)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/unauthorized')
        return request.status_code


    def open_link_forbidden(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_FORBIDDEN)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/forbidden')
        return request.status_code


    def open_link_not_found(self):
        link = self.element_is_visible(self.locators.LINK_STATUS_NOT_FOUND)
        self.go_to_element(link)
        link.click()
        request = requests.get('https://demoqa.com/invalid-url')
        return request.status_code
