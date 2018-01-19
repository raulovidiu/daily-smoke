from pages.base_page import BasePage
from tests.config import resource_library_url
from selenium.webdriver.common.by import By


class ResourceLibraryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_resource_library(self):
        self._visit(resource_library_url)

    _resource_library_breadcrumb = {"by": By.CSS_SELECTOR, "value": "span.app"}
    _product_number_input = {"by": By.CSS_SELECTOR, "value": 'input[name="catalogNumber"]'}
    _lot_number_input = {"by": By.CSS_SELECTOR, "value": 'input[name="lotId"]'}
    _download_certificate_button = {"by": By.CSS_SELECTOR, "value": 'button[value="Download Certificate"]'}

    def is_at_resource_library_page(self):
        return self._is_displayed(self._resource_library_breadcrumb)

    def download_certificate(self, product_num, lot_num):
        self._type(self._product_number_input, product_num)
        self._type(self._lot_number_input, lot_num)
        self._wait_for_is_displayed(self._download_certificate_button, 10)
        self._click(self._download_certificate_button)
