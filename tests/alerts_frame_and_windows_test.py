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
            alert_page = AlertsPage(driver, 'https://demoqa.com/browser-windows')
            alert_page.open()