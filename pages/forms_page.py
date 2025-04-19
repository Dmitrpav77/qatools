import os
import random

from generator.generator import generated_person
from locators.forms_page_locators import FormsPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time



class FormsPage(BasePage):
    locators = FormsPageLocators()

    def fill_the_form(self):
        person = next(generated_person())
        file_path = rf'O:\pet_project\picture{random.randint(0, 999)}.jpeg'
        file = open(file_path, 'w+')
        file.close()
        subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology",
        "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies",
        "History", "Civics"]
        first_name = person.first_name
        last_name = person.last_name
        email = person.email
        mobile = person.mobile
        date_of_birth = person.date_of_birth
        address = person.current_address
        self.go_to_element(self.element_is_visible(self.locators.INPUT_FIRSTNAME))
        self.element_is_visible(self.locators.INPUT_FIRSTNAME).send_keys(first_name)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_LASTNAME))
        self.element_is_visible(self.locators.INPUT_LASTNAME).send_keys(last_name)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_EMAIL))
        self.element_is_visible(self.locators.INPUT_EMAIL).send_keys(email)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_GENDER))
        self.element_is_visible(self.locators.INPUT_GENDER).click()
        self.go_to_element(self.element_is_visible(self.locators.INPUT_MOBILE))
        self.element_is_visible(self.locators.INPUT_MOBILE).send_keys(mobile)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_DATE_OF_BIRTH))
        self.element_is_visible(self.locators.INPUT_DATE_OF_BIRTH).send_keys(date_of_birth)
        self.element_is_visible(self.locators.INPUT_DATE_OF_BIRTH).send_keys(Keys.ENTER)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_SUBJECTS))
        self.element_is_visible(self.locators.INPUT_SUBJECTS).click()
        data_subjects = []
        num = random.randint(3, 7)
        while num != 0:
            subject = subjects.pop(random.randint(0, len(subjects)-1))
            data_subjects.append(subject)
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(subject)
            time.sleep(1)
            self.element_is_visible(self.locators.INPUT_SUBJECTS).send_keys(Keys.ENTER)
            num -= 1
        self.go_to_element(self.element_is_visible(self.locators.INPUT_HOBBIES))
        self.element_is_visible(self.locators.INPUT_HOBBIES).click()
        self.go_to_element(self.element_is_visible(self.locators.INPUT_UPLOAD_PICTURE))
        self.element_is_present(self.locators.INPUT_UPLOAD_PICTURE).send_keys(file_path)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS))
        self.element_is_visible(self.locators.INPUT_CURRENT_ADDRESS).send_keys(address)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_STATE_DIV))
        self.element_is_visible(self.locators.INPUT_STATE_DIV).click()
        for _ in range(random.randint(5, 20)):
            self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.DOWN)
        self.element_is_visible(self.locators.INPUT_STATE).send_keys(Keys.ENTER)
        self.go_to_element(self.element_is_visible(self.locators.INPUT_CITY_DIV))
        for _ in range(random.randint(5, 20)):
            self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.DOWN)
        self.element_is_visible(self.locators.INPUT_CITY).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_visible(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        os.remove(file_path)
        return first_name + ' ' + last_name, email


    def check_output(self):
        output = self.elements_are_present(self.locators.OUTPUT_LIST)
        data = []
        for i in range(len(output)):
            if i % 2 != 0:
                data.append(output[i].text)
            else:
                continue
        return data