import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from collections import Counter

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

    def emptycart():
        driver.find_element_by_class_name ("boxshopcart").click()
        driver.find_element_by_link_text ("Empty Cart").click()

    def test_find_many(self, driver)
        driver.get("https://www.iceyarns.com/")
        emptycart() #Just in case the test failed before, this will ensure an empty cart
        # There are 19 items on the opening page + "Show More")
        for item in range(19):
            driver.find_elements_by_class_name ("tag-discount").click()
            form_element = driver.find_element_by_xpath("//form[@class='productcart']/input[range]").click()    
        
        time.sleep(2) # Let the user actually see something!
        emptycart()
        quit()