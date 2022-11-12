from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.base_page import BasePage


class HomePage(BasePage):

    HOMEPAGE_TITLE = 'Amazon.com. Spend less. Smile more.'
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@id='nav-signin-tooltip']/a/span")
    HELLO_MESSAGE = (By.ID, 'nav-link-accountList-nav-line-1')

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

    def search_after(self, query):
        self.wait_and_fill_elem_by_selector(*self.SEARCH_BOX, query)
        self.driver.find_element(*self.SEARCH_BOX).send_keys(Keys.ENTER)
        sleep(1)
