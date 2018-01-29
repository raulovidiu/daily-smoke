import pytest
import time

from pages import resource_library_page


class TestDownloadCertificate():
    @pytest.fixture()
    def resource_library_page(self, driver):
        return resource_library_page.ResourceLibraryPage(driver)

    def test_download_certificate(self, resource_library_page):
        resource_library_page.navigate_to_resource_library()
        resource_library_page.is_at_resource_library_page()

        print("Resource Library page fully loaded")
        resource_library_page._take_screenshot("41_resource_library_page_loaded.png")
        resource_library_page.download_certificate(645687, 785785)

        resource_library_page._take_screenshot("42_provided_incorrect_certificate_values.png")

        assert resource_library_page._lookup_form_error_present()
