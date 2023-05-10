import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


@pytest.mark.usefixtures("setup_and_teardown")
class AccountPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    logout_button_element_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"
    success_message_element_xpath = "//h1[normalize-space()='Your Account Has Been Created!']"

    def success_message_after_register(self):
        return self.display_status_of_element(self.success_message_element_xpath)
    def logout_option_displaying_after_login(self):
        return self.display_status_of_element(self.logout_button_element_xpath)