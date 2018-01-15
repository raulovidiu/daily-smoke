import time
from selenium.webdriver.common.by import By

from base_page import BasePage
from tests.config import product_1_url, product_2_url, product_3_url


class ProductPage(BasePage):
    _product_title = {"by": By.CSS_SELECTOR,
                      "value": "div.product-details.page-title > div.name.product-details--name > h1 > span"}
    _product_id = {"by": By.CSS_SELECTOR, "value": "div.name.product-details--name > span"}
    _product_price = {"by": By.CSS_SELECTOR,
                      "value": "div.product-details--container > div.row > div:nth-child(3) > div > div > p"}
    _add_to_cart = {"by": By.CSS_SELECTOR, "value": "#addToCartButton"}
    _close_button = {"by": By.CSS_SELECTOR, "value": "#cboxClose"}

    def ___init___(self, driver):
        self.driver = driver

    def navigate_to_product1_page(self):
        self._visit(product_1_url)
        time.sleep(1)

    def navigate_to_product2_page(self):
        self._visit(product_2_url)
        time.sleep(1)

    def navigate_to_product3_page(self):
        self._visit(product_3_url)
        time.sleep(1)

    def get_product_title(self):
        return self._get_text(self._product_title)

    def get_product_id(self):
        return self._get_text(self._product_id)

    def get_product_price(self):
        return self._get_text(self._product_price)

    def click_on_add_to_cart_button(self):
        return self._click(self._add_to_cart)

    def click_on_close_button(self):
        return self._click(self._close_button)
