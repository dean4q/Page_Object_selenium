import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from .pages.base_page import BasePage

from .pages.main_page import MainPage
from .pages.product_page import *


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    browser.implicitly_wait(3)
    page.solve_quiz_and_get_code()


