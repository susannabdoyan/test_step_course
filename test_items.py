import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30) 
    button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    
    assert button is not None, "message"
