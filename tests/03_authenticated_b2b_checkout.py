import pytest
import time

from helpers import utils_methods
from pages import store_and_region_section, b2b_login_page, b2b_family_page, header_section, product_page, \
    checkout_page, order_confirmation_page


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
    def header(self, driver):
        return header_section.Header(driver)

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

    def test_b2b_client_checkout(self, store_and_region, b2b_login, b2b_family, header, product, checkout_section, order_confirmation_page, save_order_information_to_file):
        b2b_login.navigate_to_b2b_login_page()

        store_and_region.choose_business_store()
        store_and_region.choose_united_states_region_b2b()

        b2b_login.login_as_a_b2b_user("cosmin.milchis@usource.ro", "Test@123a")
        time.sleep(10)
        print("\n The B2B user successfully authenticated")

        b2b_family.add_b2b_product1_in_cart()
        b2b_family.click_on_continue_shopping()
        print ("\n Product was successfully added to cart")

        b2b_family.add_b2b_product2_in_cart()
        b2b_family.click_on_continue_shopping()
        print ("\n Product was successfully added to cart")

        b2b_family.add_b2b_product3_in_cart()
        b2b_family.click_on_view_in_cart()
        print ("\n Product was successfully added to cart")

        product.click_on_checkout_in_cart()
        product.click_on_checkout_in_cart()
        print("\n B2B user successfully reached the Checkout section")

        checkout_section.b2b_checkout_flow("123")
        print ("\n B2B user successfully got through the checkout flow")

        print("\n" + order_confirmation_page.return_order_id())

        print ("\n B2C user placed the order and successfully transitioned to the order confirmation page")

        the_returned_order_id = order_confirmation_page.return_order_id()
        save_order_information_to_file.b2b_save_order_information(the_returned_order_id)









