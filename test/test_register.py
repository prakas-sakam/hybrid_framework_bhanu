from datetime import datetime
import pytest

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    #register with all mandetory fields
    def test_registre_with_mandetory_details(self):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        registerpage = homepage.register_element_in_my_account()
        accountpage = registerpage.enter_all_data_for_register("prakas","reddy", self.generate_email_with_timestamp(), "09976667656", "0000", "0000")
        s_message = accountpage.success_message_after_register()
        assert s_message

    #without accepting privecy polocy
    def test_without_accepting_privecy(self):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        registerpage = homepage.register_element_in_my_account()
        registerpage.continue_button()
        e_message = registerpage.error_message_for_privacy_policy()
        assert e_message


    #register with existing email fields
    def test_registre_with_existing_email_details(self):
        homepage = HomePage(self.driver)
        homepage.my_account_dropdown()
        registerpage = homepage.register_element_in_my_account()
        registerpage.first_name_field("reddy")
        registerpage.last_name_field("praksh")
        registerpage.email_name_field("s.prakasreddy@gmail.com")
        registerpage.mobile_field("0987654321")
        registerpage.password_field("12884")
        registerpage.confirm_password_field("12884")
        registerpage.privacy_policy_field()
        registerpage.continue_button()
        ee_message = registerpage.error_message_email_alredy_register()
        assert ee_message


    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        return "bhanu"+time_stamp+"@gmail.com"


