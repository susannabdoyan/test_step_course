#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By
import time
from .page_object.main_page import MainPage
from .page_object.product_page import ProductPage

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com"
#    page = MainPage(browser, link)
#    page.open()
#    login_page = page.go_to_login_page()
#    login_page.should_be_login_page()
#
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    login_page = page.should_see_login_link()
#    login_page.should_see_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.element_in_basket()
    page.basket_is_empty()
#    time.sleep(50)


#    browser.get(link)
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()
