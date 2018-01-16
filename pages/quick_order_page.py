import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QuickOrderPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _quick_order_button = {"by": By.CSS_SELECTOR,
                           "value": 'body > main > header > div.nav--top-level-wrap > nav > div.yCmsContentSlot.nav__actions.hidden-xs.hidden-sm > a.btn.btn-link.btn--quick-order.Analytics-Navigation.Secondary'}
    _product1_field= {"by": By.CSS_SELECTOR, "value": "li:nth-child(2) > div.item-sku-input.js-sku-container > input.js-sku-input-field.form-control"}
    _product2_field = {"by": By.CSS_SELECTOR, "value": "li:nth-child(3) > div.item-sku-input.js-sku-container > input.js-sku-input-field.form-control"}
    _product3_field = {"by": By.CSS_SELECTOR, "value": "li:nth-child(4) > div.item-sku-input.js-sku-container > input.js-sku-input-field.form-control"}
    _add_to_cart_button = {"by": By.CSS_SELECTOR, "value": "#js-add-to-cart-quick-order-btn-bottom"}
    _checkout = {"by": By.CSS_SELECTOR, "value": ".btn.btn-primary.add-to-cart-button"}

    def place_an_order_in_the_quick_order_page(self, product1, product2, product3):
        self._click(self._quick_order_button)
        self._type(self._product1_field, product1)
        time.sleep(5)
        self._type(self._product2_field, product2)
        time.sleep(5)
        self._type(self._product3_field, product3)
        self._press_enter_button(self._product3_field)
        time.sleep(5)
        self._wait_for_is_displayed(self._add_to_cart_button, 5)
        self._click(self._add_to_cart_button)
        self._wait_for_is_displayed(self._checkout, 5)
        self._click(self._checkout)
