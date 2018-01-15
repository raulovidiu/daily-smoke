from selenium.webdriver.common.by import By
from base_page import BasePage


class StoreAndRegionSection(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    # Elements belonging to the Please Select a Channel Overlay
    _select_channel_overlay = {'by': By.ID, 'value': 'cboxLoadedContent'}
    _select_consumer_store_button = {'by': By.ID, 'value': 'chooseB2Cbutton'}
    _select_business_store_button = {'by': By.ID, 'value': 'chooseB2Bbutton'}

    # Elements belonging to the Please Select a Region Page
    _united_states_link = {'by': By.CSS_SELECTOR, 'value': '.region:nth-child(1) a[href *="/b2c/US/en"]'}

    def choose_consumer_store(self):
        self._wait_for_is_displayed(self._select_consumer_store_button, 5)
        return self._click(self._select_consumer_store_button)

    def choose_united_states_region(self):
        self._wait_for_is_displayed(self._united_states_link, 5)
        return self._click(self._united_states_link)
