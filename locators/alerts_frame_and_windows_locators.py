from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_TAB_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')



class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    ALERT_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    CONFIRM_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_BOX_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    PROMPT_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    RESULT_FRAME_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

    # nested frames

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'body')


class ModalDialogPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    CLOSE_SMALL_MODAL_DIALOG = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    CLOSE_LARGE_MODAL_DIALOG = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
