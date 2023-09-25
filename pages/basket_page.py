import pytest
from selenium import webdriver
from .base_page import  *
from .locators import *

class BasketPage(BasePage):


    def check_empty_basket_assert_text(self):
        assert_text = self.browser.find_element(*AddToBasket.ASSERT_EMPTY_BASKET)
        answer = assert_text.text

        language = self.get_lang_from_script_page()
        if language == "ar":
            assert language == answer
        elif language == "ca":
            assert language == answer
        elif language == "cs":
            assert language == answer
        elif language == "da":
            assert language == answer
        elif language == "de":
            assert language == answer
        elif language == "en":
            assert language == answer
        elif language == "el":
            assert language == answer
        elif language == "es":
            assert language == answer
        elif language == "fi":
            assert language == answer
        elif language == "fr":
            assert language == answer
        elif language == "it":
            assert language == answer
        elif language == "ko":
            assert language == answer
        elif language == "nl":
            assert language == answer
        elif language == "pl":
            assert language == answer
        elif language == "pt":
            assert language == answer
        elif language == "pt-br":
            assert language == answer
        elif language == "ro":
            assert language == answer
        elif language == "ru":
            assert language == answer
        elif language == "sk":
            assert language == answer
        elif language == "uk":
            assert language == answer
        elif language == "zh-cn":
            assert language == answer





    def check_empty_basket(self):
        element = self.browser.find_elements(*AddToBasket.BASKET_ITEMS)
        assert len(element) == 0, "Basket is not empty, but must be empty"

