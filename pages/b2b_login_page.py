from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.config import login_url_b2b


class B2BLoginPage(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _usename_input_field = {"by": By.CSS_SELECTOR, "value": 'input[name="username"]'}
    _password_input_field = {"by": By.CSS_SELECTOR, "value": 'input[name="password"]'}
    _login_button = {"by": By.CSS_SELECTOR, "value": ".button.button-primary.Analytics-Login"}

    def navigate_to_b2b_login_page(self):
        self._visit(login_url_b2b)

    def login_as_a_b2b_user(self, email, password):
        self._type(self._usename_input_field, email)
        self._type(self._password_input_field, password)
        self._wait_for_is_displayed(self._login_button, 10)
        self._click(self._login_button)
