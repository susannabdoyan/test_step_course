from selenium.webdriver.common.by import By

class ProductPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_LINK1 = (By.CSS_SELECTOR, ".btn-group>a")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".basket-items h3 a")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.ID, "#messages div:first-child")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_page")
    REGISTER_LINK = (By.ID, "login_link")
    REGISTER_MAIL = (By.NAME, "registration-email")
    REGISTER_PASSWD1 = (By.NAME, "registration-password1")
    REGISTER_PASSWD2 = (By.NAME, "registration-password2")
    BUTTON = (By.NAME, "registration_submit")
    MESSAGE = (By.ID, "logout_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "p")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_page")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    def should_be_register_form(self):
        register_fom = self.browser.current_url
        assert register_url, "register url is not presented"

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" not in login_url, "Login url is not presented"

