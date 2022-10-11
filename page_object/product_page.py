import time
import pytest
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        print("add to basket after math")
        self.solve_quiz_and_get_code()

    def add_to_basket(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        print("user cant see success message")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                                    "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCSSESEFUL_MESSAGE),\
                                    "Success message is not disappeared"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()
        print("login page")

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def element_in_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_ITEMS)
            print("element in basket")
        except (NoSuchElementException):
            return False
        return True
    
    def basket_is_empty(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_EMPTY)
            print("Your basket is empty.")
        except (NoSuchElementException):
            return False
        return True

