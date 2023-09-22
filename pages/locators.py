from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class AddToBasket():
    ADDTOBASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main> h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main> p")
    CHECK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    CHECK_MASSAGE = (By.CSS_SELECTOR, "#messages .alert")