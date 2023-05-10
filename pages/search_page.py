import pytest
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup_and_teardown")
class SearchPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    hp_result_element_xpath = "//a[normalize-space()='HP LP3065']"
    no_product_found_element_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def finding_result_is_displayed(self):
        return self.display_status_of_element(self.hp_result_element_xpath)

    def result_not_found_for_unknown_element(self):
        return self.display_status_of_element(self.no_product_found_element_xpath)
