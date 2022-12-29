from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    DELETE_BTN = (By.CSS_SELECTOR, ".sc-action-delete .a-color-link")
    EMPTY_CART_MSG = (By.XPATH, "//h1[contains(.,'Your Amazon Cart is empty.')]")

    def click_on_delete(self):
        self.wait_and_click_elem_by_selector(*self.DELETE_BTN)

    def empty_cart_msg(self):
        self.verify_element_is_displayed_by_selector(*self.EMPTY_CART_MSG)

