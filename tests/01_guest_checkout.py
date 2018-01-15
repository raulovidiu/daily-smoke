import pytest

from pages import product_page


class TestGuestCheckout():
    @pytest.fixture()
    def product(self, driver):
        return product_page.ProductPage(driver)

    def test_elements(self, product):
        product.navigate_to_product1_page()
        product.click_on_close_button()
        assert ("Product Number 3470" == product.get_product_id())
