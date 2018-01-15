from selenium.webdriver.common.by import By
from base_page import BasePage

class StoreAndRegionSection(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Elements belonging to the Please Select a Channel Overlay
    _select_channel_overlay = {'by': By.ID, 'value': 'cboxLoadedContent'}
    _select_consumer_store_button = {'by': By.ID, 'value': 'chooseB2Cbutton'}
    _select_business_store_button = {'by': By, 'value': 'chooseB2Bbutton'}

    # Elements belonging to the Please Select a Region Page
    _united_states_link = {'by': By.CSS_SELECTOR, 'value': '.region:nth-child(1) a[href *="/b2c/US/en"]'}

    def choose_consumer_store(self):
        self._wait_for_is_displayed(self._select_consumer_store_button)
        return self._click(self._select_consumer_store_button)

    def choose_united_states_region(self):
        self._wait_for_is_displayed(self._united_states_link)
        return self._click(self._select_consumer_store_button)
