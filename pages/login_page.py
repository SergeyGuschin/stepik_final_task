
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        substring = "login"
        assert substring in current_url, "The substring not found in URL"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not present"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration Form is not present"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_thank_you_message(self):
        thank_you_message = self.browser.find_element(*LoginPageLocators.THANK_YOU_MESSAGE).text
        assert "Thanks for registering!" in thank_you_message, \
            '"Thanks for registering!" message  not present in the page after registration.'

    def should_be_account_link_in_the_header_site(self):
        assert self.is_element_present(*LoginPageLocators.ACCOUNT_LINK_IN_THE_HEADER), \
            "No Account link in the header"
