import time
from time import process_time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    BrokenLinksPage


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

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            webtable_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            webtable_page.open()
            new_person = webtable_page.add_new_person(1)
            time.sleep(3)
            find_new_person = webtable_page.find_person(new_person[0])
            time.sleep(3)
            assert new_person in find_new_person, 'New person had not been found'


        def test_web_table_edit_person(self, driver):
            webtable_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            webtable_page.open()
            new_person = webtable_page.add_new_person(1)
            webtable_page.find_person(new_person[0])
            edited_person = webtable_page.edit_person()
            find_edited_person = webtable_page.find_person(edited_person[0])
            assert edited_person in find_edited_person


        def test_web_table_delete_person(self, driver):
            webtable_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            webtable_page.open()
            new_person = webtable_page.add_new_person(1)
            webtable_page.find_person(new_person[0])
            webtable_page.delete_person()
            webtable_page.find_person(new_person[0])
            search_result = webtable_page.check_search_result()
            print(search_result)
            assert search_result == "No rows found"

    class TestButtons:
        def test_buttons_click(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double_click = buttons_page.double_click_on_button()
            right_click = buttons_page.right_click_on_button()
            dynamic_click = buttons_page.dynamic_click_on_button()
            assert double_click == "You have done a double click", 'There is no match after double click'
            assert right_click == "You have done a right click", 'There is not match after right click'
            assert dynamic_click == "You have done a dynamic click", 'There is not match after dynamic click'

    class TestLinks:
        def test_new_tab_simple(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link = links_page.open_new_tab_simple_link()
            links_page.switch_to_new_blank(1)
            url_new_tab = links_page.check_current_url()
            assert href_link == url_new_tab, 'The url of new tab does not match to href'


        def test_new_tab_dynamic(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link = links_page.open_new_tab_dynamic_link()
            links_page.switch_to_new_blank(1)
            url_new_tab = links_page.check_current_url()
            assert href_link == url_new_tab, 'The url of new tab does not match to href'


        def test_link_created(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_created = links_page.open_link_created()
            assert status_created == 201, 'The status code of response is not 201'


        def test_link_forbidden(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_forbidden = links_page.open_link_forbidden()
            assert status_forbidden == 403, 'The status code of response is not 403'


        def test_link_moved(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_moved = links_page.open_link_moved()
            assert status_moved == 301, 'The status code of response is not 301'


        def test_link_not_found(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_not_found = links_page.open_link_not_found()
            assert status_not_found == 404, 'The status code of response is not 404'


        def test_link_no_content(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_no_content = links_page.open_link_no_content()
            assert status_no_content == 204, 'The status code of response is not 204'


        def test_link_bad_request(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_bad_request = links_page.open_link_bad_request()
            assert status_bad_request == 400, 'The status code of response is not 400'


        def test_link_unauthorized(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            status_unauthorized = links_page.open_link_unauthorized()
            assert status_unauthorized == 401, 'The status code of response is not 401'


    class TestBrokenLinks:
        def test_image_is_not_broken(self, driver):
            links_page = BrokenLinksPage(driver, 'https://demoqa.com/broken')
            links_page.open()
            picture_is_not_broken = links_page.get_size_valid_image()
            assert True == picture_is_not_broken, 'The picture is broken'


        def test_image_is_broken(self, driver):
            links_page = BrokenLinksPage(driver, 'https://demoqa.com/broken')
            links_page.open()
            picture_is_broken = links_page.get_size_broken_image()
            assert True == picture_is_broken, 'The picture is not broken'


        def test_valid_link(self, driver):
            links_page = BrokenLinksPage(driver, 'https://demoqa.com/broken')
            links_page.open()
            status_code, url = links_page.open_valid_link()
            assert status_code == 200 and url == "https://demoqa.com/", "The link is not valid"


        def test_broken_link(self, driver):
            links_page = BrokenLinksPage(driver, 'https://demoqa.com/broken')
            links_page.open()
            status_code, url = links_page.open_broken_link()
            assert status_code == 500, "The status code is not correct"


