from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_element = x_element.text

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x_element))

    RobCheck = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    RobCheck.click()

    RobRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    RobRule.click()

    Button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    Button.click()

finally:
    time.sleep(10)
    browser.quit()



