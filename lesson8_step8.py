from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    firstname.send_keys('kek')

    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys('kek')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('kek@memes.com')

    file = browser.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname('lesson8_step8.py'))
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()