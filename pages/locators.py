from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_YOUR_BASKET_SUCCES_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")


