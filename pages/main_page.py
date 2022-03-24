from pages.base_page import BasePage
from pages.locators import MainPageLocators

LOGIN_LINK = MainPageLocators.LOGIN_LINK


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

