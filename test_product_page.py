import time
import pytest
from .page_object.base_page import BasePage
from .page_object.main_page import MainPage
from .page_object.product_page import ProductPage
from .page_object.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    "Test user can add product to basket"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    "Test guest can add product to basket"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()                      
    page.add_product_to_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    "Test guest can go to login page from product page"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    "Test guest cant see product in basket opened from product page"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.element_in_basket()
    page.basket_is_empty()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    def test_user_registration(browser):
        "Test user registration"
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.test_register_new_user()
    
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        "Test user cant see seccess message after adding product to pasket"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        "Test user cant see seccess message"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

