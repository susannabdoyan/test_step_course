import time
import pytest
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
    def test_register_new_user(self):
        link = self.browser.find_element(*ProductPageLocators.REGISTER_LINK)
        link.click()
        link1 = self.browser.find_element(*ProductPageLocators.REGISTER_MAIL)
        link1.send_keys("bdoyansus1166@gmail.com")
        link2 = self.browser.find_element(*ProductPageLocators.REGISTER_PASSWD1)
        link2.send_keys("sus123sus")
        link3 = self.browser.find_element(*ProductPageLocators.REGISTER_PASSWD2)
        link3.send_keys("sus123sus")
        button1 = self.browser.find_element(*ProductPageLocators.BUTTON)
        button1.click()
        time.sleep(5)
        assert self.browser.find_element(*ProductPageLocators.MESSAGE) != "logout_link", "registration failed"
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        LoginPageLocators.should_be_login_url 

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True 
