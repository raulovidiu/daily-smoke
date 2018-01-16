import os
import time

class SaveOrderInformationToFile:
    def save_order_information(order_id):
        f = open("/Users/usource/Desktop/daily-smoke/screenshots/order_artifacts.txt", "a")
        f.write("Order Number is " + order_id + ", and was placed at " + time.ctime())
        f.write('\n')
        f.close()
