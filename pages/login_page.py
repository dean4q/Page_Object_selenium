from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "registration form is not presented"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        email_field = self.email.find_element(*LoginPageLocators.EMAIL_INPUT_FIELD) #поиск поля ввода имейл
        email_field.sendkeys(self.email)          #заполнение поля имейл
        password_field = self.password.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD)
        password_field.sendkeys(self.password)     #заполнение поля с паролем
        confirm_password_field = self.password.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT_FIELD)
        confirm_password_field.sendkeys(self.password) #заполнение поля с паролем 2
        button = self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON)
        button.click()
