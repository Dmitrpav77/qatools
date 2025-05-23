import time

from pages.widgets_page import WidgetsPage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_accordian_text, second_accordian_text, third_accordian_text = accordian_page.accordian_check()
            assert first_accordian_text > 0, 'There is no text in first accordian'
            assert second_accordian_text > 0, 'There is no text in second accordian'
            assert third_accordian_text > 0, 'There is no text in third accordian'

    class TestAutoComplete:
        def test_autocomplete_multiple_colors(self, driver):
            autocomplete_page = WidgetsPage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            input_amount = autocomplete_page.check_autocomplete(3)
            time.sleep(3)
            count_amount = autocomplete_page.count_multi_input()
            assert input_amount == count_amount, 'Colors have not selected'

        def test_autocomplete_single_color(self, driver):
            autocomplete_page = WidgetsPage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            selected_single_color = autocomplete_page.check_autocomplete_single_color()
            selected_single_color_text = autocomplete_page.check_selected_single_color_text()
            assert selected_single_color == selected_single_color_text, 'Color has not selected'

