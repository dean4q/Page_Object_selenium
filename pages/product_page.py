import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import AddToBasket
from selenium.common.exceptions import NoAlertPresentException
import math
class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def add_product_to_basket(self):
        button_add_basket = self.browser.find_element(*AddToBasket.ADDTOBASKET)
        button_add_basket.click()

    def find_product_name(self):
        name = self.browser.find_element(*AddToBasket.PRODUCT_NAME)
        product_name = name.text
        return product_name

    def find_product_price(self):
        price = self.browser.find_element(*AddToBasket.PRODUCT_PRICE)
        product_price = price.text
        return product_price

    def check_equal_product_name(self):
        name = self.browser.find_element(*AddToBasket.CHECK_NAME)
        alert_name = name.text
        return alert_name