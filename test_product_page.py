import time

import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from .pages.base_page import BasePage

from .pages.main_page import MainPage
from .pages.product_page import *


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]



@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()


    assert page.find_product_name() == page.check_equal_product_name()
    # print()
    # print("Цена книги", page.find_product_price())
