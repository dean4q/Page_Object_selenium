from .base_page import BasePage
from .locators import *
from .login_page import LoginPage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

