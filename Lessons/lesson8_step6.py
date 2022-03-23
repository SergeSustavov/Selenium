from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

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
    browser.execute_script("return arguments[0].scrollIntoView(true);", RobRule)
    RobRule.click()

    Button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", Button)
    Button.click()

finally:
    time.sleep(5)
    browser.quit()