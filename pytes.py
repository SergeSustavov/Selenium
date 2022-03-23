from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


link = "http://suninjuly.github.io/registration1.html"


class TestRegistration1():

    @pytest.mark.regression
    def test_inputs(self, browser):
        browser.get(link)

        element_1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        element_1.send_keys('kek')

        element_2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        element_2.send_keys('kek')

        element_3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        element_3.send_keys('kek')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text

        assert "Congratulations! You have successfully registered!" == welcome_text, 'Failed'

