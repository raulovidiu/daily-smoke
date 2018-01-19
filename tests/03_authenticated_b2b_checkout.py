import pytest
import time

from helpers import utils_methods
from pages import store_and_region_section, b2b_login_page, b2b_family_page, product_page, \
    checkout_page, order_confirmation_page
from tests.config import b2b_username, b2b_password


class TestAuthenticatedB2bCheckout():
    @pytest.fixture()
    def store_and_region(self, driver):
        return store_and_region_section.StoreAndRegionSection(driver)

    @pytest.fixture()
    def b2b_login(self, driver):
        return b2b_login_page.B2BLoginPage(driver)

    @pytest.fixture()
    def b2b_family(self, driver):
        return b2b_family_page.B2BFamilyPage(driver)

    @pytest.fixture()
    def product(self, driver):
        return product_page.ProductPage(driver)

    @pytest.fixture()
    def checkout_section(self, driver):
        return checkout_page.Checkout(driver)

    @pytest.fixture()
    def order_confirmation_page(self, driver):
        return order_confirmation_page.OrderConfirmationPage(driver)

    @pytest.fixture()
    def save_order_information_to_file(self, driver):
        return utils_methods.SaveOrderInformationToFile(driver)

    def test_b2b_client_checkout(self, store_and_region, b2b_login, b2b_family, product, checkout_section, order_confirmation_page, save_order_information_to_file):
        b2b_login.navigate_to_b2b_login_page()
        b2b_login._take_screenshot("27_on_login_page.png")

        store_and_region.choose_business_store()
        store_and_region._take_screenshot("28_selecting_business_store.png")
        store_and_region.choose_united_states_region_b2b()
        store_and_region._take_screenshot("29_selecting_usa_region.png")

        b2b_login.login_as_a_b2b_user(b2b_username, b2b_password)
        time.sleep(10)
        print("\n The B2B user successfully authenticated")
        b2b_family._take_screenshot("29_b2b_authenticated.png")

        b2b_family.add_b2b_product1_in_cart()
        b2b_family._take_screenshot("30_first_product_added.png")
        b2b_family.click_on_continue_shopping()
        b2b_family._take_screenshot("31_click_on_continue_shopping.png")
        print ("\n Product was successfully added to cart")

        b2b_family.add_b2b_product2_in_cart()
        b2b_family._take_screenshot("32_second_product_added.png")
        b2b_family.click_on_continue_shopping()
        b2b_family._take_screenshot("33_click_on_continue_shopping.png")
        print ("\n Product was successfully added to cart")

        b2b_family.add_b2b_product3_in_cart()
        b2b_family._take_screenshot("34_third_product_added.png")
        b2b_family.click_on_view_in_cart()
        b2b_family._take_screenshot("35_proceeding_to_cart.png")
        print ("\n Product was successfully added to cart")

        product.click_on_checkout_in_cart()
        product._take_screenshot("36_proceeding_to_cart.png")
        product.click_on_checkout_in_cart()
        print("\n B2B user successfully reached the Checkout section")

        checkout_section.b2b_checkout_flow("123")
        checkout_section._take_screenshot("37_checking_out.png")
        print ("\n B2B user successfully got through the checkout flow")

        print("\n" + order_confirmation_page.return_order_id())
        order_confirmation_page._take_screenshot("38_on_order_confirmation_page.png")

        print ("\n B2C user placed the order and successfully transitioned to the order confirmation page")

        the_returned_order_id = order_confirmation_page.return_order_id()
        save_order_information_to_file.b2b_save_order_information(the_returned_order_id)
