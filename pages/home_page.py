import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_page import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    search_box_element_xpath = "//input[@placeholder='Search']"
    search_button_element_xpath = "//button[@class='btn btn-default btn-lg']"
    my_account_element_xpath = "//i[@class='fa fa-user']"
    login_element_xpath = "//a[normalize-space()='Login']"
    register_element_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']"
    def search_box_data_enter(self,data):
        self.type_into_element(data,self.search_box_element_xpath)

    def clicking_search_button(self):
        self.click_element(self.search_button_element_xpath)
        return SearchPage(self.driver)
    def my_account_dropdown(self):
        self.click_element(self.my_account_element_xpath)
    def login_element_in_my_account(self):
        self.click_element(self.login_element_xpath)
        return LoginPage(self.driver)
    def register_element_in_my_account(self):
        self.click_element(self.register_element_xpath)
        return RegisterPage(self.driver)

    def search_for_product(self,data):
        self.search_box_data_enter(data)
        self.clicking_search_button()
        return SearchPage(self.driver)