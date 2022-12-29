from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'ap_email')
    CONTINUA_BTN = (By.ID, 'continue')
    PASSWORD_INPUT = (By.ID, 'ap_password')
    SIGN_IN_BTN = (By.ID, 'signInSubmit')

    def set_email(self):
        email = 'davidtstacct@gmail.com'
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def click_continua_btn(self):
        self.wait_and_click_elem_by_selector(*self.CONTINUA_BTN)

    def set_password(self):
        password = 'aMaz7!on'
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_sign_in_btn(self):
        self.wait_and_click_elem_by_selector(*self.SIGN_IN_BTN)
