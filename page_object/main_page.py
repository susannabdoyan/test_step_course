from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .login_page import LoginPage

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPage)
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(*LoginPage)
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(*LoginPage), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_see_login_link(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

