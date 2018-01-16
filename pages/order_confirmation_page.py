from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderConfirmationPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _order_id = {"by": By.CSS_SELECTOR, "value": '.checkout-success__body > p:first-of-type b'}

    def return_order_id(self):
        self._wait_for_is_displayed(self._order_id, 15)
        return self._get_text(self._order_id)
