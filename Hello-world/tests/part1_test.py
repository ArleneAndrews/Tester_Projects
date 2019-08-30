import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Firefox session
driver = webdriver.Firefox(executable_path='E:\Documents and Settings\mom\geckodriver-v0.24.0-win64')
driver.implicitly_wait(30)
driver.maximize_window()

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