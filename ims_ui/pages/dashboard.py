from selenium.webdriver.common.by import By

from .basepage import BasePage


class Dashboard(BasePage):

    _sign_out_selector = (By.CLASS_NAME, 'icon-icon_Sign_Out')

    expected_title = 'Invincea Management'

    def confirm_page(self):
        self.get_element(self._sign_out_selector)

