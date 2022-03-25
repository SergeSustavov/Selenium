from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

LOGIN_FROM = LoginPageLocators.LOGIN_FORM
REGISTER_FORM = LoginPageLocators.REGISTER_FORM
EMAIL = LoginPageLocators.EMAIL
PASSWORD_REG1 = LoginPageLocators.PASSWORD_REG1
PASSWORD_REG2 = LoginPageLocators.PASSWORD_REG2
REG_SUBMIT = LoginPageLocators.REG_SUBMIT


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

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(By.CSS_SELECTOR, EMAIL)
        email_form.send_keys(email)

        password_form1 = self.browser.find_element(By.CSS_SELECTOR, PASSWORD_REG1)
        password_form1.send_keys(password)

        password_form2 = self.browser.find_element(By.CSS_SELECTOR, PASSWORD_REG2)
        password_form2.send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, REG_SUBMIT).click()




