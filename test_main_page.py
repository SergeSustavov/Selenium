from pages.main_page import MainPage
from selenium import webdriver


def test_guest_can_login(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main = MainPage(browser, url)
    main.open()
    main.go_to_login_page()
