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