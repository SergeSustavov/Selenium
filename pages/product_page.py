from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

PRODUCT_TITLE = ProductPageLocators.PRODUCT_TITLE
PRODUCT_PRICE = ProductPageLocators.PRODUCT_PRICE
ADD_TO_CART_BUTTON = ProductPageLocators.ADD_TO_CART_BUTTON
MESSAGE_PRODUCT_ADDED = ProductPageLocators.MESSAGE_PRODUCT_ADDED
ADDED_PRODUCT_TITLE = ProductPageLocators.ADDED_PRODUCT_TITLE
CART_COST = ProductPageLocators.CART_COST
CART_VALUE = ProductPageLocators.CART_VALUE


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(By.CSS_SELECTOR, ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_product_added_to_cart(self):
        assert self.is_element_present(By.CSS_SELECTOR, MESSAGE_PRODUCT_ADDED)
        assert self.browser.find_element(By.CSS_SELECTOR, PRODUCT_TITLE).text == \
               self.browser.find_element(By.CSS_SELECTOR, ADDED_PRODUCT_TITLE).text
        assert self.is_element_present(By.CSS_SELECTOR, CART_COST)
        assert self.browser.find_element(By.CSS_SELECTOR, PRODUCT_PRICE).text == \
               self.browser.find_element(By.CSS_SELECTOR, CART_VALUE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, MESSAGE_PRODUCT_ADDED), \
            'Success message is presented, but should not be'

    def should_success_message_disappear(self):
        assert self.is_disappeared(By.CSS_SELECTOR, MESSAGE_PRODUCT_ADDED), \
            'Success message did not disappear'
