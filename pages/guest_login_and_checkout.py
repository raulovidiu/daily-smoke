from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginAndCheckOut(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _email_address_input = {'by': By.CSS_SELECTOR, 'value': 'input[name="email"]'}
    _confirm_email_address_input = {'by': By.CSS_SELECTOR, 'value': '.confirmGuestEmail.form-control'}
    _checkout_guest_button = {'by': By.CSS_SELECTOR, 'value': '.btn.btn-default.btn-block.guestCheckoutBtn'}

    def checkout_as_guest(self, email, confirmed_email):
        self._type(self._email_address_input, email)
        self._click(self._confirm_email_address_input)
        self._type(self._confirm_email_address_input, confirmed_email)
        self._click(self._checkout_guest_button)
