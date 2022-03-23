from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import math
import time

dict_links = ['https://stepik.org/lesson/236895/step/1',
              'https://stepik.org/lesson/236896/step/1',
              'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1',
              'https://stepik.org/lesson/236899/step/1',
              'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1',
              'https://stepik.org/lesson/236905/step/1]']


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', dict_links)
class TestingAnswer:
    def test_feedback(self, browser, links):
        browser.get(links)
        text = browser.find_element(By.CSS_SELECTOR, '[placeholder="Type your answer here..."]')
        text.send_keys(math.log(int(time.time())))
        button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
        button.click()

        feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
        assert feedback == 'Correct!'
