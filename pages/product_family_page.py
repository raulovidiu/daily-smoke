from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.config import product_family_page_link


class ProductFamilyPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _5ml_option = {"by": By.CSS_SELECTOR, "value": ".productSpecifications__group:nth-child(2) ul li:nth-child(3)"}
    _individually_wrapped_clear_plastic_option = {"by": By.CSS_SELECTOR, "value": ".productSpecifications__group:nth-child(3) ul li:nth-child(2)"}
    _product_number = {"by": By.CSS_SELECTOR, "value": 'span[class="tablesaw-cell-content"] > a'}
    _add_to_cart_button = {"by": By.CSS_SELECTOR, "value": 'button[class="addToCart js-enable-btn"]'}
    _facebook_icon = {"by": By.CSS_SELECTOR, "value": 'span[class="social-icon corn-icon-fa-facebook"]'}

    def navigate_to_product_family_page(self):
        self._visit(product_family_page_link)

    def select_specifications(self):
        self._click(self._5ml_option)
        self._click(self._individually_wrapped_clear_plastic_option)

    def product_id(self):
        return self._get_text(self._product_number)

    def return_list_of_elems(self):
        _elems = self.driver.find_elements_by_css_selector('button[class="addToCart js-enable-btn"]')
        if len(_elems) == 1:
            print("\n Only the " + self.product_id() + " is present in the Products table")
        else:
            print("\n The list has: " + len(_elems) + " products.")
