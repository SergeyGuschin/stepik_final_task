from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
    THANK_YOU_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    ACCOUNT_LINK_IN_THE_HEADER = (By.XPATH, "//a[normalize-space()='Account']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_YOUR_BASKET_SUCCES_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_PRESENTS_ON_THE_BASKET_PAGE = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
