import pytest
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage


@pytest.mark.usefixtures("setup_and_teardown")
class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_element_xpath = "//input[@id='input-firstname']"
    last_name_element_xpath = "//input[@id='input-lastname']"
    email_element_xpath = "//input[@id='input-email']"
    phone_element_xpath = "//input[@id='input-telephone']"
    password_element_xpath = "//input[@id='input-password']"
    confirm_password_element_xpath = "//input[@id='input-confirm']"
    privacy_policy_element_xpath = "//input[@name='agree']"
    continue_element_xpath = "//input[@value='Continue']"
    error_message_to_agree_privacy_policy_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    error_message_email_already_register_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def first_name_field(self,f_name):
        self.type_into_element(f_name, self.first_name_element_xpath)
    def last_name_field(self,l_name):
        self.type_into_element(l_name, self.last_name_element_xpath)
    def email_name_field(self,email):
        self.type_into_element(email, self.email_element_xpath)
    def mobile_field(self,number):
        self.type_into_element(number, self.phone_element_xpath)
    def password_field(self,password):
        self.type_into_element(password, self.password_element_xpath)
    def confirm_password_field(self,conf_pass):
        self.type_into_element(conf_pass, self.confirm_password_element_xpath)
    def privacy_policy_field(self):
        self.click_element(self.privacy_policy_element_xpath)
    def continue_button(self):
        self.click_element(self.continue_element_xpath)
        return AccountPage(self.driver)

    def error_message_for_privacy_policy(self):
        return self.display_status_of_element(self.error_message_to_agree_privacy_policy_xpath)
    def error_message_email_alredy_register(self):
        return self.display_status_of_element(self.error_message_email_already_register_xpath)

    def enter_all_data_for_register(self,first_name,l_name, email, phone, password,confirm_pass,):
        self.first_name_field(first_name)
        self.last_name_field(l_name)
        self.email_name_field(email)
        self.mobile_field(phone)
        self.password_field(password)
        self.confirm_password_field(confirm_pass)
        self.privacy_policy_field()
        newpage = self.continue_button()
        if newpage.__eq__(AccountPage(self.driver)):
            return AccountPage(self.driver)
        else:
            return