from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    def should_be_register_form(self):
        register_fom = self.browser.current_url
        #assert register_url, "register url is not presented"

    def should_be_login_url(self):
        login_url = self.browser.current_url
        #assert "login" not in login_url, "Login url is not presented"
