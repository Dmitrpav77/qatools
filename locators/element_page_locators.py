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

class WebtablePageLocators:

    # add new person
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # find person
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    ALL_TABLE_ROWS = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')


    # edit person
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    # delete person
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')

class ButtonsPageLocators:

    DOUBLE_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    DYNAMIC_CLICK = (By.XPATH, '//div[3]/button')
    OUTPUT_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    OUTPUT_RIGHT_CLICK = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    OUTPUT_DYNAMIC_CLICK = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

class LinksPageLocators:

    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_LINK = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    LINK_STATUS_CREATED = (By.CSS_SELECTOR, 'a[id="created"]')
    LINK_STATUS_NO_CONTENT = (By.CSS_SELECTOR, 'a[id="no-content"]')
    LINK_STATUS_MOVED = (By.CSS_SELECTOR, 'a[id="moved"]')
    LINK_STATUS_BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    LINK_STATUS_UNAUTHORIZED = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    LINK_STATUS_FORBIDDEN = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    LINK_STATUS_NOT_FOUND = (By.CSS_SELECTOR, 'a[id="invalid-url"]')

class BrokenLinksPageLocators:

    VALID_PICTURE = (By.XPATH, '//div[2]/header/a/img')
    BROKEN_PICTURE = (By.XPATH, '//div[2]/img[2]')
    VALID_LINK = (By.CSS_SELECTOR, 'a[href="http://demoqa.com"]')
    BROKEN_LINK = (By.CSS_SELECTOR, 'a[href="http://the-internet.herokuapp.com/status_codes/500"]')

class UploadDownloadPageLocators:
    UPLOAD_INPUT = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

class DynamicPropertiesPageLocators:
    DYNAMIC_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')


