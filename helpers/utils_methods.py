import os
import time
from pages.base_page import BasePage
from tests.config import local_order_artifacts_guest, local_order_artifacts_b2c, local_order_artifacts_b2b


class SaveOrderInformationToFile(BasePage):
    def ___init___(self, driver):
        self.driver = driver

    def guest_save_order_information(self, order_id):
        f = open(local_order_artifacts_guest, "a")
        f.write("Order Number is " + order_id + ", and was placed at " + time.ctime())
        f.write('\n')
        f.close()

    def b2c_save_order_information(self, order_id):
        f = open(local_order_artifacts_b2c, "a")
        f.write("Order Number is " + order_id + ", and was placed at " + time.ctime())
        f.write('\n')
        f.close()

    def b2b_save_order_information(self, order_id):
        f = open(local_order_artifacts_b2b, "a")
        f.write("Order Number is " + order_id + ", and was placed at " + time.ctime())
        f.write('\n')
        f.close()
