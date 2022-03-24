from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

LOGIN_LINK = MainPageLocators.LOGIN_LINK


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        return self.is_element_present(By.CSS_SELECTOR, LOGIN_LINK), "Login link is not presented"
