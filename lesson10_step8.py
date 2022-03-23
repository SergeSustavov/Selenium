from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x_element = x_element.text

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x_element))

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

    alert2 = browser.switch_to.alert
    print(alert2.text.split(':')[-1].strip())

finally:
    browser.quit()


