import pytest

from helpers import utils_methods
from pages import product_page, header_section, store_and_region_section, guest_login_and_checkout_page, checkout_page, \
    order_confirmation_page


class TestGuestCheckout():
    @pytest.fixture()
    def product(self, driver):
        return product_page.ProductPage(driver)

    @pytest.fixture()
    def header_section(self, driver):
        return header_section.Header(driver)

    @pytest.fixture()
    def store_and_region(self, driver):
        return store_and_region_section.StoreAndRegionSection(driver)

    @pytest.fixture()
    def guest_login_checkout(self, driver):
        return guest_login_and_checkout_page.LoginAndCheckOut(driver)

    @pytest.fixture()
    def checkout(self, driver):
        return checkout_page.Checkout(driver)

    @pytest.fixture()
    def order_confirmation_page(self, driver):
        return order_confirmation_page.OrderConfirmationPage(driver)

    @pytest.fixture()
    def save_order_information_to_file(self, driver):
        return utils_methods.SaveOrderInformationToFile(driver)

    def test_guest_checkout(self, product, header_section, store_and_region, guest_login_checkout, checkout, order_confirmation_page, save_order_information_to_file):
        product.navigate_to_product1_page()
        product._take_screenshot("01_product_page_1.png")
        store_and_region.choose_consumer_store()
        store_and_region._take_screenshot("02_choose_consumer_store.png")
        store_and_region.choose_united_states_region_b2c()
        store_and_region._take_screenshot("03_choose_united_states_region.png")
        assert ("Product Number 3470" == product.get_product_id())

        product.click_on_add_to_cart_button()
        product._take_screenshot("04_adding_first_product_to_cart.png")
        product.click_on_continue_shopping()
        product._take_screenshot("05_clicking_on_continue_overlay.png")
        print ("\n Product" + product.get_product_id() + " was successfully added to cart")
        product.navigate_to_product2_page()
        product._take_screenshot("06_product_page_2.png")
        assert ("(1)" == header_section.get_product_count())
        assert ("Product Number 356243" == product.get_product_id())

        product.click_on_add_to_cart_button()
        product._take_screenshot("07_adding_second_product_to_cart.png")
        product.click_on_continue_shopping()
        product._take_screenshot("08_clicking_on_continue_overlay.png")
        print ("Product" + product.get_product_id() + " was successfully added to cart")

        product.navigate_to_product3_page()
        product._take_screenshot("09_product_page_3.png")
        assert ("(2)" == header_section.get_product_count())
        assert ("Product Number 1000-100" == product.get_product_id())

        product.click_on_add_to_cart_button()
        product._take_screenshot("10_adding_third_product_to_cart.png")
        print ("Product" + product.get_product_id() + " was successfully added to cart")
        product.click_on_checkout()
        product._take_screenshot("11_proceeding_to_cart.png")
        assert ("(3)" == header_section.get_product_count())
        print ("\n Guest successfully transitioned to the cart page")

        product.click_on_checkout_in_cart()
        product._take_screenshot("12_proceeding_to_checkout.png")

        guest_login_checkout.checkout_as_guest("cmilchis@siteworx.com", "cmilchis@siteworx.com")
        print ("\n Guest successfully authenticated")
        guest_login_checkout._take_screenshot("13_guest_authenticated.png")

        print ("\n Guest successfully transitioned to the checkout page")

        checkout.add_new_address("United States", "Mr.", "Tester", "Test", "Siteworx", "Plopilor 63", "Portland", "Oregon", "54321")
        checkout._take_screenshot("14_provided_new_address.png")

        checkout.add_card_details("Visa", "4111111111111111", "12", "2019", "113")
        checkout._take_screenshot("15_provided_credit_card_details.png")

        print ("\n Guest successfully got through the checkout flow")

        print("\n" + order_confirmation_page.return_order_id())

        print ("\n Guest placed the order and successfully transitioned to the order confirmation page")
        order_confirmation_page._take_screenshot("16_on_order_confirmation_page.png")

        the_returned_order_id = order_confirmation_page.return_order_id()
        save_order_information_to_file.guest_save_order_information(the_returned_order_id)
