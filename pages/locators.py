from selenium.webdriver.common.by import By


class MainPageLocators():
    LANGUAGE = (By.CSS_SELECTOR, "")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_TO_BASKET_LINK = (By.XPATH, "/html/body/header/div/div/div[2]/span/a")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_FIELD = (By.NAME, 'registration-email')
    PASSWORD_INPUT_FIELD =(By.NAME, 'registration-password1')
    CONFIRM_PASSWORD_INPUT_FIELD = (By.NAME, 'registration-password2')
    REGISTR_BUTTON = (By.NAME, 'registration_submit')
    LOG_IN_BUTTON = (By.NAME, 'login_submit')


class AddToBasket():
    ADDTOBASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main> h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main> p")
    CHECK_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    CHECK_MASSAGE = (By.CSS_SELECTOR, "#messages .alert")
    ASSERT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")