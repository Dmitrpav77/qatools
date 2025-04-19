import random
import time
from selenium.webdriver.common.keys import Keys

from locators.alerts_frame_and_windows_locators import AlertsPageLocators, BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def new_tab_click(self):
        self.go_to_element(self.element_is_visible(self.locators.NEW_TAB_BUTTON))
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()

    def check_new_tab_text(self):
        self.switch_to_new_blank(1)
        new_tab_text = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        return new_tab_text

    def new_window_click(self):
        self.go_to_element(self.element_is_visible(self.locators.NEW_WINDOW_BUTTON))
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()

    def check_new_window_text(self):
        self.switch_to_new_blank(1)
        new_window_text = self.element_is_present(self.locators.NEW_WINDOW_TEXT).text
        return new_window_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def see_the_alert(self):
        alert = self.element_is_visible(self.locators.ALERT_BUTTON)
        alert.click()
        alert_text = self.driver.switch_to.alert
        return alert_text.text


    def see_the_alert_after_5_sec(self):
        alert = self.element_is_visible(self.locators.ALERT_5_SEC_BUTTON)
        alert.click()
        time.sleep(5)
        alert_text = self.driver.switch_to.alert
        return alert_text.text


    def accept_confirm_alert(self):
        confirm_alert = self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON)
        confirm_alert.click()
        confirm = self.driver.switch_to.alert
        confirm.accept()


    def dismiss_confirm_alert(self):
        confirm_alert = self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON)
        confirm_alert.click()
        confirm = self.driver.switch_to.alert
        confirm.dismiss()

    def check_confirm_result(self):
        result = self.element_is_present(self.locators.CONFIRM_BOX_RESULT)
        return result.text


    def prompt_alert(self):
        prompt = self.element_is_visible(self.locators.PROMPT_BOX_BUTTON)
        prompt.click()
        prompt_alert = self.driver.switch_to.alert
        name = f'Name{random.randint(0, 100)}'
        prompt_alert.send_keys(name)
        prompt_alert.accept()
        return name

    def check_result_prompt_alert(self):
        result = self.element_is_present(self.locators.PROMPT_BOX_RESULT)
        return result.text



