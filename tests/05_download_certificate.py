import pytest
import time

from pages import resource_library_page
from tests.config import certificate_product_number, certificate_lot_number


class TestDownloadCertificate():
    @pytest.fixture()
    def resource_library_page(self, driver):
        return resource_library_page.ResourceLibraryPage(driver)

    def test_download_certificate(self, resource_library_page):
        resource_library_page.navigate_to_resource_library()
        resource_library_page.is_at_resource_library_page()

        print("Resource Library page fully loaded")
        resource_library_page._take_screenshot("39_resource_library_page_loaded.png")

        resource_library_page.download_certificate(certificate_product_number, certificate_lot_number)

        print("Downloading certificate")
        resource_library_page._take_screenshot("40_downloading_certificate.png")
