import time
import pytest

from .pages.login_page import *
from .pages.basket_page import BasketPage
from .pages.base_page import *
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#
#
class TestUserAddToBasketFromProductPage():
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.add_product_to_basket()
        # page.solve_quiz_and_get_code()

        assert page.find_product_name() == page.check_equal_product_name()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_base_link)
        page.open()
        page.should_not_be_success_message()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): #ложноположительный тест
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()



@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):     #текст не изчезает после добавления в корзину товара
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/visual-guide-to-lock-picking_206/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_empty_basket()
    page.check_empty_basket_assert_text()

class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = 'q1w2e3r4t5y6u7i'
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
