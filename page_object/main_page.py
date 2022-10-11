from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
