"""Implementing Login screen page objects"""

from TestFramework.Libraries.Pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    # Start: Login page locators
    sign_in_button_locator = (By.ID, "signinButton")
    email_field_locator = (By.ID, "ap_email")
    password_field_locator = (By.ID, "ap_password")
    login_button_locator = (By.ID, "signInSubmit")
    logout_button_locator = (By.XPATH, "//a[text()='Sign out']")
    # End: Login page locators

    def is_user_loggedin(self):
        """
        Check if the user is already logged in or not
        :return: True/False
        """
        user_is_loggedin = None
        timeout = time.time() + self.get_time_out_value()
        while time.time() < timeout:
            if self.is_element_present(self.login_button_locator, time_out=5):
                user_is_loggedin = False
                break
            else:
                if self.is_element_present(self.logout_button_locator, time_out=5):
                    user_is_loggedin = True
                    break

        return user_is_loggedin

    def perform_login(self, user_name, password):
        """
        Implementing Login functionality
        :param user_name:
        :param password:
        :return:
        """
        # if self.is_user_loggedin() is True:
        #     pass
        # else:
        self.click_element(self.sign_in_button_locator)
        self.set_value_into_input_field(self.email_field_locator, user_name)
        self.set_value_into_input_field(self.password_field_locator, password)
        self.click_element(self.login_button_locator)