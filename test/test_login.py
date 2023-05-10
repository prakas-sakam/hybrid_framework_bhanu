import pytest
from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities import excelUtil


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Login:
#login with valid email and password
    @pytest.mark.parametrize("email_address, password", excelUtil.get_data_from_excel("xlfiles/tutorialsninja.xlsx", "login"))
    def test_loginwith_valid_credentials(self, email_address, password):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        loginpage = homepage.login_element_in_my_account()
        accountpage = loginpage.enter_email_and_password_for_login_on_success(email_address, password)
        logout_display = accountpage.logout_option_displaying_after_login()
        assert logout_display

    #llogin with invalid email and valid password
    def test_loginwith_invalid_email_credentials(self):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        loginpage = homepage.login_element_in_my_account()
        aleret_message = loginpage.enter_email_and_password_for_login_on_failure("ss@gmail.com", "0987654")
        assert aleret_message

    #llogin with no email and no password
    def test_loginwith_no_credentials(self):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        loginpage = homepage.login_element_in_my_account()
        loginpage.login_button_clicking()
        aleret_message = loginpage.error_message_by_wrong_details()
        assert aleret_message
