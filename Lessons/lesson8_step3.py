from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
# link = 'http://suninjuly.github.io/selects2.html'


def calc(num1, num2):
    value = int(num1) + int(num2)
    return str(value)


try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(calc(num1, num2))

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()