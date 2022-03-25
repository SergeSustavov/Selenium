class BasePageLocators():
    LOGIN_LINK = "#login_link"
    BASKET = 'span a.btn.btn-default'
    USER_ICON = ".icon-user"

class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = '#content_inner'

class MainPageLocators():
    LOGIN_LINK = "#login_link"


class LoginPageLocators():
    LOGIN_FORM = '#login_form'
    REGISTER_FORM = '#register_form'
    EMAIL = '#id_registration-email'
    PASSWORD_REG1 = '#id_registration-password1'
    PASSWORD_REG2 = '#id_registration-password2'
    REG_SUBMIT = "[name='registration_submit']"

class ProductPageLocators():
    PRODUCT_TITLE = '.product_main h1'
    PRODUCT_PRICE = '.product_main .price_color'
    ADD_TO_CART_BUTTON = 'button.btn-add-to-basket'
    MESSAGE_PRODUCT_ADDED = '#messages> :nth-child(1) '
    ADDED_PRODUCT_TITLE = MESSAGE_PRODUCT_ADDED + 'strong'
    CART_COST = '#messages> :nth-child(3) '
    CART_VALUE = CART_COST + 'strong'
