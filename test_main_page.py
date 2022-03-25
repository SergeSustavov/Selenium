from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_login(self, browser):
        main = MainPage(browser, url)
        main.open()
        main.go_to_login_page()
        login = LoginPage(browser, url)
        login.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, url)
        page.open()
        assert page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, url)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
