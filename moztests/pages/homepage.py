from selenium.webdriver.common.by import By

from .basepage import BasePage
from .technology_page import TechnologyPage


class HomePage(BasePage):

    _username_selector = (By.NAME, 'username')
    _password_selector = (By.NAME, 'password')
    _sign_in_button_selector = (By.CSS_SELECTOR, 'input.btn')

    def login(self, username, password):
        self.enter_text(self._username_selector, username)
        self.enter_text(self._password_selector, password)
        self.click(self._sign_in_button_selector)
        return TechnologyPage(self.driver, self.variables)
