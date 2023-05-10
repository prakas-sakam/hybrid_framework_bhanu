from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def type_into_element(self,text,locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def display_status_of_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element.is_displayed()