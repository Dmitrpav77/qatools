import time

from pages.alerts_frame_and_windows_page import AlertsPage, BrowserWindowPage


class TestAlertsFrameWindows:
    class TestBrowserWindow:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            new_tab_page.new_tab_click()
            new_tab_text = new_tab_page.check_new_tab_text()
            assert new_tab_text == 'This is a sample page', 'texts do not match'


        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            new_window_page.new_window_click()
            new_window_text = new_window_page.check_new_window_text()
            assert new_window_text == 'This is a sample page', 'texts do not match'



    class TestAlerts:
        def test_alert_page(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.see_the_alert()
            assert alert_text == 'You clicked a button', 'The button has not clicked or the alert has not displayed'


        def test_alert_after_5_sec_page(self, driver):
            alert_5_sec_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_5_sec_page.open()
            alert_text = alert_5_sec_page.see_the_alert_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'The button has not clicked or the alert has not displayed'


        def test_accept_confirm_alert(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            confirm_alert_page.accept_confirm_alert()
            result_confirm = confirm_alert_page.check_confirm_result()
            assert result_confirm == 'You selected Ok', 'Alert did not show up'


        def test_dismiss_confirm_alert(self, driver):
            confirm_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            confirm_alert_page.open()
            confirm_alert_page.dismiss_confirm_alert()
            result_confirm = confirm_alert_page.check_confirm_result()
            assert result_confirm == 'You selected Cancel', 'Alert did not show up'


        def test_prompt_alert(self, driver):
            prompt_alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            prompt_alert_page.open()
            input_name = prompt_alert_page.prompt_alert()
            result = prompt_alert_page.check_result_prompt_alert()
            assert f'You entered {input_name}' == result, 'Alert did not show up'
