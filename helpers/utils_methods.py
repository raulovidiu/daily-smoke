import os
import time
from pages.base_page import BasePage


class SaveOrderInformationToFile(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    def save_order_information(self, order_id):
        f = open("/Users/usource/Desktop/daily-smoke/screenshots/order_artifacts.txt", "a")
        f.write("Order Number is " + order_id + ", and was placed at " + time.ctime())
        f.write('\n')
        f.close()
