from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    # RESULTS_TITLE = (By.XPATH, '//a[@data-zone="title"]')

    def verify_results_contain_text(self, text):
        products_list = self.driver.find_elements(By.PARTIAL_LINK_TEXT, text)
        for i in range(3):
            title = products_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')
