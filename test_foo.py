#import pytest
import time
from .page_object.main_page import MainPage
from .page_object.product_page import ProductPage

#@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "", "8", "9"])
#def test_guest_can_add_product_to_basket(browser, link):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#    page = ProductPage(browser, link)
#    page.open()                      
#    page.add_product_to_basket()

#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_be_login_link()
#
#def test_guest_can_go_to_login_page_from_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.element_in_basket()
    page.basket_is_empty()
