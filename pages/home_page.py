from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    ACCEPT_COOKIES_BTN = (By.CSS_SELECTOR, '.inline-block > .button-wrapper')
    NEWSLETTER_CLOSE_BTN = (By.CSS_SELECTOR, 'button.p-1')
    HOMEPAGE_TITLE = (By.CSS_SELECTOR, 'Electronice si electrocasnice online la cel mai mic pret')
    SEARCH_BOX = (By.CSS_SELECTOR, '[placeholder="Cauta produsul dorit"]')

    def navigate_to_home_page(self):
        self.driver.get('https://altex.ro/home/')

    def click_accept_cookies_btn(self):
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)

    def click_newsletter_close_btn(self):
        self.click_if_present_by_selector(*self.NEWSLETTER_CLOSE_BTN)

    def home_page_title(self):
        self.driver.find_element(*self.HOMEPAGE_TITLE)

    def search_box(self):
        self.driver.find_element(*self.SEARCH_BOX)

    def verify_url_message(self):
        self.verify_page_url('https://altex.ro/home/')

