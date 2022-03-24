from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

LOGIN_FROM = LoginPageLocators.LOGIN_FORM
REGISTER_FORM = LoginPageLocators.REGISTER_FORM


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Wrong URL'

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, LOGIN_FROM), 'Login form is not displayed'

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, REGISTER_FORM), 'Register form is not displayed'
