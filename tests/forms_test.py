from pages.forms_page import FormsPage


class TestForms:
    class TestFormPage:
        def test_fill_the_form(self, driver):
            form_page = FormsPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_name, person_email = form_page.fill_the_form()
            output_result = form_page.check_output()
            assert person_name and person_email in output_result, 'The info about person and output data do not match'