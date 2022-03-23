from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    go_to_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    go_to_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_element = x_element.text

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x_element))

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

    alert2 = browser.switch_to.alert
    print(alert2.text.split(':')[-1].strip())

finally:
    browser.quit()



