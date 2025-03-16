import time
from time import process_time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.get_output_fields_text()
            assert full_name == output_full_name, 'fullname and output fullname do not match'
            assert email == output_email, 'email and output email do not match'
            assert current_address == output_current_address, 'current address and output current address do not match'
            assert permanent_address == output_permanent_address, 'permanent address and output permanent address do not match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.expand_all()
            check_box_page.random_click_checkbox()
            input_checkbox = check_box_page.get_title_selected_checkboxes()
            output_result = check_box_page.get_title_output_checkboxes()
            assert input_checkbox == output_result, "The selected checkboxes are not consistent with the result."

    class TestRadioButton:
        def test_radiobutton(self, driver):
            radiobutton_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radiobutton_page.open()
            radiobutton_yes = radiobutton_page.random_radiobutton_click("Yes")
            output_result_yes = radiobutton_page.get_output_result()
            radiobutton_impressive = radiobutton_page.random_radiobutton_click("Impressive")
            output_result_impressive = radiobutton_page.get_output_result()
            radiobutton_no = radiobutton_page.random_radiobutton_click("No")
            output_result_no = radiobutton_page.get_output_result()
            assert radiobutton_yes == output_result_yes, "The radiobutton 'Yes' had not been selected"
            assert radiobutton_impressive == output_result_impressive, "The radiobutton 'Impressive' had not been selected"
            assert radiobutton_no == output_result_no, "The radiobutton 'No' had not been selected"

