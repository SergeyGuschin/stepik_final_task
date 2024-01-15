from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCTS_PRESENTS_ON_THE_BASKET_PAGE), \
            "The Basket is not empty"

    def should_be_empty_basket_message(self):
        empty_cart_test = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty" in empty_cart_test, "The empty basket message is wrong"
