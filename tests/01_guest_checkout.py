import pytest

from pages import product_page, header, store_and_region_section


class TestGuestCheckout():
    @pytest.fixture()
    def product(self, driver):
        return product_page.ProductPage(driver)

    @pytest.fixture()
    def header_section(self, driver):
        return header.Header(driver)

    @pytest.fixture()
    def store_and_region(self, driver):
        return store_and_region_section.StoreAndRegionSection(driver)

    def test_guest_checkout(self, product, header_section, store_and_region):
        product.navigate_to_product1_page()
        store_and_region.choose_consumer_store()
        store_and_region.choose_united_states_region()
        assert ("Product Number 3470" == product.get_product_id())

        product.click_on_add_to_cart_button()
        product.click_on_continue_shopping()
        print ("\n Product" + product.get_product_id() + " was successfully added to cart")
        product.navigate_to_product2_page()
        assert ("(1)" == header_section.get_product_count())
        assert ("Product Number 356243" == product.get_product_id())

        product.click_on_add_to_cart_button()
        product.click_on_continue_shopping()
        print ("Product" + product.get_product_id() + " was successfully added to cart")

        product.navigate_to_product3_page()
        assert ("(2)" == header_section.get_product_count())
        assert ("Product Number 1000-100" == product.get_product_id())

        product.click_on_add_to_cart_button()
        print ("Product" + product.get_product_id() + " was successfully added to cart")
        product.click_on_checkout()
        assert ("(3)" == header_section.get_product_count())

        product.click_on_checkout_in_cart()
