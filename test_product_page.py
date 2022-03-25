import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_product_added_to_cart()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_cart()
    time.sleep(2)
    product_page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, url)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser):
        create_email = str(time.time()) + "@fakemail.org"
        create_password = 'awdaAWD0120'
        self.login = LoginPage(browser, url)
        self.login.open()
        self.login.go_to_login_page()
        self.login.register_new_user(create_email, create_password)
        time.sleep(3)
        self.login.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.add_to_cart()
        product_page.check_product_added_to_cart()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = BasketPage(browser, url)
        page.open()
        page.go_to_basket()
        page.basket_is_empty()
