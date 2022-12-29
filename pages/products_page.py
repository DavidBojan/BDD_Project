from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def verify_results_contain_text(self, text):
        products_list = self.driver.find_elements(By.PARTIAL_LINK_TEXT, text)
        for i in range(3):
            title = products_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def click_on_product(self, product):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, product).click()

    def add_to_cart(self):
        self.click_if_present_by_selector(*self.ADD_TO_CART)
