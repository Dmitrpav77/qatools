from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.get_output_fields_text()
            assert full_name == output_full_name, 'fullname and output fullname are not equal'
            assert email == output_email, 'email and output email are not equal'
            assert current_address == output_current_address, 'current address and output current address are not equal'
            assert permanent_address == output_permanent_address, 'permanent address and output permanent address are not equal'