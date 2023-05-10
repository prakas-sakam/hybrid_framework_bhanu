import pytest
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage


@pytest.mark.usefixtures("setup_and_teardown")
class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    email_element_xpath = "//input[@id='input-email']"
    password_element_xpath = "//input[@id='input-password']"
    login_button_element_xpath = "//input[@value='Login']"
    alert_message_element_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def email_field(self, e_mail):
        self.type_into_element(e_mail, self.email_element_xpath)

    def password_field(self, password):
       self.type_into_element(password, self.password_element_xpath)
    def login_button_clicking(self):
        self.click_element(self.login_button_element_xpath)
        return AccountPage(self.driver)

    def error_message_by_wrong_details(self):
        return self.display_status_of_element(self.alert_message_element_xpath)

    def enter_email_and_password_for_login_on_success(self,email,password):
        self.email_field(email)
        self.password_field(password)
        self.login_button_clicking()
        return AccountPage(self.driver)
    def enter_email_and_password_for_login_on_failure(self,email,password):
        self.email_field(email)
        self.password_field(password)
        self.login_button_clicking()
        return self.error_message_by_wrong_details()