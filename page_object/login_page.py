from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        LoginPageLocators.should_be_login_url 

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        LoginPageLocators.should_be_register_form

    def should_see_login_link(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

