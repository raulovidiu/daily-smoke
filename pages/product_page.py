import time
from selenium.webdriver.common.by import By

from base_page import BasePage
from tests.config import product_1_url, product_2_url, product_3_url


class ProductPage(BasePage):
    _product_id = {"by": By.CSS_SELECTOR, "value": "div.name.product-details--name > span"}
    _add_to_cart = {"by": By.ID, "value": "addToCartButton"}
    _continue_shopping = {"by": By.CSS_SELECTOR,
                          "value": "#addToCartLayer > div.flex-container > a.btn.btn-link.js-mini-cart-close-button"}
    _checkout = {"by": By.CSS_SELECTOR, "value": "a.btn.btn-primary.add-to-cart-button"}
    _checkout_in_cart = {"by": By.CSS_SELECTOR,
                         "value": "div.col-sm-12.col-md-6.cart-actions--print.cart__actions > button.btn.btn-primary.btn-block.btn--continue-checkout.js-continue-checkout-button"}

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

    def get_product_id(self):
        return self._get_text(self._product_id)

    def click_on_add_to_cart_button(self):
        return self._click(self._add_to_cart)

    def click_on_continue_shopping(self):
        self._wait_for_is_displayed(self._continue_shopping, 60)
        return self._click(self._continue_shopping)

    def click_on_checkout(self):
        self._wait_for_is_displayed(self._checkout, 60)
        return self._click(self._checkout)

    def click_on_checkout_in_cart(self):
        self._wait_for_is_displayed(self._checkout_in_cart, 60)
        return self._click(self._checkout_in_cart)
