from selenium.webdriver.common.by import By


class WidgetsPageLocators:
    # accordian locators
    FIRST_ACCORDIAN = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND_ACCORDIAN = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    THIRD_ACCORDIAN = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_ACCORDIAN_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

    # autocomplete multiple colors
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_INPUT_AMOUNT = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')

    # autocomplete single color
    INPUT_SINGLE_COLOR = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    OUTPUT_SINGLE_COLOR_TEXT = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

