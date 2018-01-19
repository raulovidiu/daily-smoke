import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Checkout(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    _payment_type_submit_button = {"by": By.ID, "value": "paymentTypeSubmit"}
    _add_new_address_button = {"by": By.CSS_SELECTOR, "value": 'button[data-toggle="#addressForm"]'}
    _country_dropdown_menu = {"by": By.CSS_SELECTOR, "value": 'select[name="countryIso"]'}
    _title_dropdown_menu = {"by": By.CSS_SELECTOR, "value": 'select[name="titleCode"]'}
    _first_name_input = {"by": By.CSS_SELECTOR, "value": 'input[name="firstName"]'}
    _last_name_input = {"by": By.CSS_SELECTOR, "value": 'input[name="lastName"]'}
    _organization_input = {"by": By.CSS_SELECTOR, "value": 'input[name="company"]'}
    _address_line_1_input = {"by": By.CSS_SELECTOR, "value": 'input[name="line1"]'}
    _town_or_city_input = {"by": By.CSS_SELECTOR, "value": 'input[name="townCity"]'}
    _state_dropdown_menu = {"by": By.CSS_SELECTOR, "value": 'select[name="regionIso"]'}
    _zip_postal_code_input = {"by": By.CSS_SELECTOR, "value": 'input[name="postcode"]'}
    _add_address_button = {"by": By.CSS_SELECTOR, "value": 'button[id="addressSubmit"]'}
    _shipping_delivery_button = {"by": By.ID, "value": "shippingDeliverySubmit"}

    _purchase_order_input = {"by": By.CSS_SELECTOR, "value": 'input[name="purchaseOrderNumber"]'}

    _delivery_method_button = {"by": By.ID, "value": "deliveryMethodSubmit"}

    _next_payment_button = {"by": By.CSS_SELECTOR, "value": ".checkout-next"}

    _card_type_dropdown = {"by": By.CSS_SELECTOR, "value": 'select[name="card_cardType"]'}
    _card_number_input = {"by": By.CSS_SELECTOR, "value": 'input[name="card_accountNumber-formatted"]'}
    _card_expiration_month_dropdown = {"by": By.CSS_SELECTOR, "value": 'select[name="card_expirationMonth"]'}
    _card_expiration_year_dropdown = {"by": By.CSS_SELECTOR, "value": 'select[name="card_expirationYear"]'}
    _security_code_input = {"by": By.CSS_SELECTOR, "value": 'input[name="card_cvNumber"]'}
    _terms_checkbox = {"by": By.CSS_SELECTOR, "value": 'input[name="termsCheck"]'}
    _place_order_button = {"by": By.CSS_SELECTOR, "value": '.checkoutSummaryButton'}

    _check_box = {"by": By.CSS_SELECTOR, "value": 'input[name="useDeliveryAddress"]'}

    def add_new_address(self, country, title, first_name, last_name, organization, address, town_or_city, state,
                        postal_code):

        # Payment Type section
        self._click(self._payment_type_submit_button)

        # Shipping Address section
        self._click(self._add_new_address_button)

        # Add New Address section
        self._wait_for_is_displayed(self._country_dropdown_menu, 60)
        self._select_dropdown_option(self._country_dropdown_menu, country)
        self._wait_for_is_displayed(self._title_dropdown_menu, 60)
        self._select_dropdown_option(self._title_dropdown_menu, title)
        self._type(self._first_name_input, first_name)
        self._type(self._last_name_input, last_name)
        self._type(self._organization_input, organization)
        self._type(self._address_line_1_input, address)
        self._type(self._town_or_city_input, town_or_city)
        self._select_dropdown_option(self._state_dropdown_menu, state)
        self._type(self._zip_postal_code_input, postal_code)
        self._click(self._add_address_button)
        self._click(self._shipping_delivery_button)

        # Shipping Method section
        self._click(self._delivery_method_button)

        # Payment & Billing Address section
        time.sleep(10)
        self._click(self._next_payment_button)

    def add_card_details(self, card_type, card_number, exp_month, exp_year, security_code):
        # Review Order section
        self._select_dropdown_option(self._card_type_dropdown, card_type)
        self._type(self._card_number_input, card_number)
        self._select_dropdown_option(self._card_expiration_month_dropdown, exp_month)
        self._select_dropdown_option(self._card_expiration_year_dropdown, exp_year)
        self._type(self._security_code_input, security_code)
        self._wait_for_is_displayed(self._terms_checkbox, 5)
        self._click(self._terms_checkbox)
        self._click(self._place_order_button)

    def b2c_checkout_flow(self):
        # Payment Type section
        self._click(self._payment_type_submit_button)

        # Shipping Address section
        self._click(self._shipping_delivery_button)

        # Shipping Method section
        self._click(self._delivery_method_button)

        # Payment & Billing Address section
        time.sleep(10)
        self._click(self._next_payment_button)

    def b2b_checkout_flow(self, payment_number):
        # Payment Type section
        self._type(self._purchase_order_input, payment_number)
        self._press_enter_button(self._purchase_order_input)
        self._wait_for_is_displayed(self._payment_type_submit_button, 10)
        self._click(self._payment_type_submit_button)

        # Shipping Method section
        time.sleep(10)
        self._wait_for_is_displayed(self._delivery_method_button, 10)
        self._click(self._delivery_method_button)

        # Review Order section
        time.sleep(10)
        self._wait_for_is_displayed(self._terms_checkbox, 10)
        self._click(self._terms_checkbox)
        self._click(self._place_order_button)



