import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import AddToBasket
from selenium.common.exceptions import NoAlertPresentException
import math
class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(10)
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
        return ProductPage(browser=self.browser, url=self.browser.current_url)

    # def should_be_answer(self):
    #     assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"