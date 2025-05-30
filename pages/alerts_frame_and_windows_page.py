import random
import time
from logging import lastResort

from selenium.webdriver.common.keys import Keys

from locators.alerts_frame_and_windows_locators import AlertsPageLocators, BrowserWindowsPageLocators, \
    FramePageLocators, ModalDialogPageLocators
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


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame_1(self):
        self.driver.switch_to.default_content()
        frame = self.element_is_visible(self.locators.FIRST_FRAME)
        self.go_to_element(frame)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        result = self.element_is_present(self.locators.RESULT_FRAME_TEXT)
        return [result.text, height, width]


    def check_frame_2(self):
        self.driver.switch_to.default_content()
        frame = self.element_is_visible(self.locators.SECOND_FRAME)
        self.go_to_element(frame)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        result = self.element_is_present(self.locators.RESULT_FRAME_TEXT)
        return [result.text, height, width]

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    def check_small_modal(self):
        small_modal_dialog = self.element_is_visible(self.locators.SMALL_MODAL)
        small_modal_dialog.click()
        small_modal = self.element_is_present(self.locators.SMALL_MODAL_TEXT)
        small_modal_text = small_modal.text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_DIALOG).click()
        return small_modal_text


    def check_large_modal(self):
        large_modal_dialog = self.element_is_visible(self.locators.LARGE_MODAL)
        large_modal_dialog.click()
        large_modal_text = self.element_is_present(self.locators.LARGE_MODAL_TEXT).text
        self.element_is_visible(self.locators.CLOSE_LARGE_MODAL_DIALOG).click()
        return large_modal_text







