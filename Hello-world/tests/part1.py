import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFindItem():

    @pytest.fixture
    def driver(self, request):
        driver_ = webdriver.Firefox()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_


    def test_enter_type(self, driver):
        driver.get("https://www.iceyarns.com/")
        driver.find_element(By.ID, "sinput2").send_keys("eyelash")
        driver.find_element(By.ID, "submit").click()