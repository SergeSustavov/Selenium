from pages.base_page import BasePage
from pages.locators import BasePageLocators
from selenium.webdriver.common.by import By
from pages.locators import BasketPageLocators

BASKET = BasePageLocators.BASKET
BASKET_IS_EMPTY_MESSAGE = BasketPageLocators.BASKET_IS_EMPTY_MESSAGE


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_element_present(By.CSS_SELECTOR, BASKET_IS_EMPTY_MESSAGE), \
            'Product is presented, but should not be'
