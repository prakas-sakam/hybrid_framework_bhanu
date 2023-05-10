import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities import ReadConfigurations


@pytest.fixture
def setup_and_teardown(request):
    driver = None
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    #driver = webdriver.Edge()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("plese choose good one in list chrome/Edge/Firefox")
    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
