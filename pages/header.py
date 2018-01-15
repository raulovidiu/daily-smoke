from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):
    _product_count = {"by": By.CSS_SELECTOR,
                      "value": "body > main > header > div.header > div > div.header__utilityNavWrap > div > div.header__utilityNav-iconWrap.header__utilityNav-iconWrap--commerce > a:nth-child(2) > span"}

    def ___init___(self, driver):
        self.driver = driver

    def get_product_count(self):
        return self._get_text(self._product_count)
