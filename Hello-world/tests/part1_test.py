import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        driver.find_element(By.ID, "sinput2").send_keys(Keys.RETURN)
        time.sleep(2) # Let the user actually see something!