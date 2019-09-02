import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Chrome session
driver = webdriver.Chrome()

class TestFindItem():

    @pytest.fixture
    def driver(self, request):
        driver_ = driver

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_


    def test_enter_type(self, driver):
        driver.get("https://www.iceyarns.com/")
        driver.find_element(By.ID, "sinput2").send_keys("eyelash")
        driver.find_element(By.ID, "submit").click()