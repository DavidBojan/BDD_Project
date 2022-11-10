from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):

    HOMEPAGE_TITLE = 'Amazon.com. Spend less. Smile more.'
    SEARCH_BOX = (By.ID, 'nav-search')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@id='nav-signin-tooltip']/a/span")
    HELLO_MESSAGE = (By.ID, 'nav-link-accountList-nav-line-1')
    # CONT_SELECTOR = (By.CSS_SELECTOR, '.truncate > .jsx-e76f220f8ec56813')
    # USERNAME_SELECTOR = (By.NAME, 'name=email')
    # USERNAME = "davidtstacct@gmail.com"
    # PASSWORD_SELECTOR = (By.NAME, 'name=password')
    # PASSWORD = "aLteX?1Pass"
    # AUTENTIFICARE_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')

    def navigate_to_home_page(self):
        self.driver.get('https://www.amazon.com/')

    def home_page_title(self):
        page_title = self.driver.title
        title_expected = self.HOMEPAGE_TITLE
        self.assertEqual(title_expected, page_title, 'Page title is incorrect')

    def search_box(self):
        self.driver.find_element(*self.SEARCH_BOX)

    def sign_in_button_displayed(self):
        self.verify_element_is_displayed_by_selector(*self.SIGN_IN_BUTTON)

    def hello_message(self):
        self.verify_element_is_displayed_by_selector(*self.HELLO_MESSAGE)

    def click_sign_in_button(self):
        self.click_if_present_by_selector(*self.SIGN_IN_BUTTON)

    #
    # def verify_url_message(self):
    #     self.verify_page_url('https://altex.ro/home/')
    #
    # def click_on_cont(self):
    #     self.click_if_present_by_selector(*self.CONT_SELECTOR)
    #
    # def set_email(self):
    #     self.wait_and_fill_elem_by_selector(*self.USERNAME_SELECTOR, self.USERNAME)
    #
    # def set_password(self):
    #     self.wait_and_fill_elem_by_selector(*self.PASSWORD_SELECTOR, self.PASSWORD)
    #
    # def click_on_autentificare(self):
    #     self.click_if_present_by_selector(*self.AUTENTIFICARE_BTN)
    #
    # def check_login_button(self):
    #     try:
    #         wait = WebDriverWait(self.driver, 10)
    #         wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.LoggedInBadge')))
    #     except TimeoutException:
    #         return False
    #     return True
