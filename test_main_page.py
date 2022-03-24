from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_login(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    main = MainPage(browser, url)
    main.open()
    main.go_to_login_page()
    login = LoginPage(browser, url)
    login.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    assert page.should_be_login_link()
