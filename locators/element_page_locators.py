from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    # form fields
    INPUT_FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    INPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    INPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    OUTPUT_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')

class CheckBoxPageLocators:

    EXPAND_ALL = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_CHECKED_ITEMS = (By.XPATH, './/span[@class="rct-title"]')
    CHECKBOX_LIST = (By.CSS_SELECTOR, 'span[class="rct-checkbox"]')
    OUTPUT_SELECTED_CHECKBOXES = (By.CSS_SELECTOR, 'span[class="text-success"]')

class RadioButtonPageLocators:

    YES_BUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_BUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')
