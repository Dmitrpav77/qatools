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

    def new_tab(self):
        pass