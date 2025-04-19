import random
from selenium.webdriver.common.by import By

class FormsPageLocators:
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    INPUT_LASTNAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    INPUT_GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{random.randint(1, 3)}"]')
    INPUT_MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    INPUT_DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    INPUT_SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    INPUT_HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    INPUT_UPLOAD_PICTURE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    INPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    #
    INPUT_STATE_DIV = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]')
    INPUT_STATE = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]/div[2]/div/input')
    INPUT_CITY_DIV = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[3]/div/div/div[1]')
    INPUT_CITY = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[3]/div/div/div[1]/div[2]/div/input')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')
    OUTPUT_LIST = (By.CSS_SELECTOR, 'tr > td')