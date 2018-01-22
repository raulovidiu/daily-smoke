import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.config import b2b_product1_url, b2b_product2_url, b2b_product3_url


class B2BFamilyPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _add_to_cart_button = {"by": By.CSS_SELECTOR, "value": '.productSpecifications__group-buttons button.addToCart'}
    _continue_shopping = {"by": By.CSS_SELECTOR,
                          "value": "#addToCartLayer > div.flex-container > a.btn.btn-link.js-mini-cart-close-button"}
    _view_cart = {"by": By.CSS_SELECTOR,
                         "value": "#addToCartLayer > div.flex-container > a.btn.btn-primary.add-to-cart-button"}

    def add_b2b_product1_in_cart(self):
        self._visit(b2b_product1_url)
        time.sleep(10)
        self._wait_for_is_displayed(self._add_to_cart_button, 15)
        self._click(self._add_to_cart_button)

    def add_b2b_product2_in_cart(self):
        self._visit(b2b_product2_url)
        time.sleep(10)
        self._wait_for_is_displayed(self._add_to_cart_button, 15)
        self._click(self._add_to_cart_button)

    def add_b2b_product3_in_cart(self):
        self._visit(b2b_product3_url)
        time.sleep(10)
        self._wait_for_is_displayed(self._add_to_cart_button, 15)
        self._click(self._add_to_cart_button)

    def click_on_continue_shopping(self):
        self._wait_for_is_displayed(self._continue_shopping, 60)
        return self._click(self._continue_shopping)

    def click_on_view_in_cart(self):
        self._wait_for_is_displayed(self._view_cart, 60)
        return self._click(self._view_cart)
