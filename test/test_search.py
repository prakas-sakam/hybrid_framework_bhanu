import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search:
    #searchin for hp
    def test_serach_for_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("hp")
        result = search_page.finding_result_is_displayed()
        assert result

    #searching for honda
    def test_serach_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("honda")
        result = search_page.result_not_found_for_unknown_element()
        assert result

    #searching without any data enter
    def test_serach_for_invalid_noproduct(self):
        home_page = HomePage(self.driver)
        search_page = home_page.clicking_search_button()
        result = search_page.result_not_found_for_unknown_element()
        assert result
