from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_cart_button.click()

    def should_be_added_to_cart_book_message(self):
        book_name_on_the_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        added_to_basket_succes_message = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_YOUR_BASKET_SUCCES_MESSAGE).text
        assert added_to_basket_succes_message == book_name_on_the_page, "Book in basket does not match book on page"

    def should_be_total_basket_price_message(self):
        book_price_on_the_page = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_total_price_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE).text
        assert basket_total_price_message == book_price_on_the_page, "Basket total price does not match product price"
