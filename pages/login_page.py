from selenium.webdriver.common.by import By
from config.settings import BASE_URL
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY = (By.ID, "inventory_container")

    def load(self):
        self.driver.get(BASE_URL)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN)
        return self

    def is_logged_in(self):
        return self.wait_visible(self.INVENTORY).is_displayed()

    def error_message(self):
        return self.get_text(self.ERROR)
