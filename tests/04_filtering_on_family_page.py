import pytest

from pages import product_family_page, store_and_region_section, resource_library_page


class TestFilteringOnFamilyPage():
    @pytest.fixture()
    def product_family(self, driver):
        return product_family_page.ProductFamilyPage(driver)

    @pytest.fixture()
    def store_and_region(self, driver):
        return store_and_region_section.StoreAndRegionSection(driver)

    @pytest.fixture()
    def resource_library_page(self, driver):
        return resource_library_page.ResourceLibraryPage(driver)

    def test_selecting_pfp_variants(self, product_family, store_and_region, resource_library_page):
        product_family.navigate_to_product_family_page()
        print("\n The user reached the product page.")
        resource_library_page._take_screenshot("41_user_reached_the_product_family_page.png")

        store_and_region.choose_business_store()
        store_and_region.choose_united_states_region_b2b()

        product_family.select_specifications()
        resource_library_page._take_screenshot("42_only_one_product_in_page.png")
        print("\n The user successfully selected the product specification")

        print("\n Only the " + product_family.product_id() + " is present in the Products table")




