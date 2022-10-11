import time
import pytest
from .page_object.main_page import MainPage
from .page_object.product_page import ProductPage

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    "Test guest cant see product in basket opened from main page"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.element_in_basket()
    page.basket_is_empty()

@pytest.mark.need_review
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):     
        "Test guest can go to login page"
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        "Test guest should see login link"
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
