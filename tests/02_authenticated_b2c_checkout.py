import pytest
import time
from helpers import utils_methods
from pages import b2c_login_page, store_and_region_section, quick_order_page, product_page, checkout_page, \
    order_confirmation_page
from tests.config import b2c_username, b2c_password


class TestAuthenticatedB2cCheckout():
    @pytest.fixture()
    def store_and_region(self, driver):
        return store_and_region_section.StoreAndRegionSection(driver)

    @pytest.fixture()
    def b2c_login(self, driver):
        return b2c_login_page.B2CLoginPage(driver)

    @pytest.fixture()
    def quick_order(self, driver):
        return quick_order_page.QuickOrderPage(driver)

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

    def test_b2c_client_checkout(self, b2c_login, store_and_region, quick_order, product, checkout_section, order_confirmation_page, save_order_information_to_file):
        b2c_login.navigate_to_b2c_login_page()
        b2c_login._take_screenshot("17_navigate_to_login_page.png")

        store_and_region.choose_consumer_store()
        store_and_region._take_screenshot("18_selecting_consumer_store.png")
        store_and_region.choose_united_states_region_b2c()
        store_and_region._take_screenshot("19_selecting_usa_region.png")

        b2c_login.login_as_a_b2c_user(b2c_username, b2c_password)
        time.sleep(10)
        print("\n The B2C user successfully authenticated")
        b2c_login._take_screenshot("20_authenticating_b2c_user.png")

        quick_order.navigate_to_b2c_quick_order_page()
        quick_order._take_screenshot("21_navigating_to_quick_order.png")

        quick_order.place_an_order_in_the_quick_order_page("6875-SB", "AP-8-200", "1000-100")
        quick_order._take_screenshot("22_place_an_order_in_the_quick_order_page.png")
        print("\n B2C user successfully added the products in the cart and reached the Cart section")

        product.click_on_checkout_in_cart()
        product._take_screenshot("23_proceeding_to_checkout.png")
        print("\n B2C user successfully reached the Checkout section")

        checkout_section.b2c_checkout_flow()
        checkout_section._take_screenshot("24_on_checkout.png")
        checkout_section.add_card_details("Visa", "4111111111111111", "12", "2019", "234")
        checkout_section._take_screenshot("25_provided_card_details.png")

        print ("\n B2C user successfully got through the checkout flow")

        print("\n" + order_confirmation_page.return_order_id())
        order_confirmation_page._take_screenshot("26_on_order_confirmation_page.png")

        print ("\n B2C user placed the order and successfully transitioned to the order confirmation page")

        the_returned_order_id = order_confirmation_page.return_order_id()
        save_order_information_to_file.b2c_save_order_information(the_returned_order_id)
