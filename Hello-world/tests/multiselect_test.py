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

    def noitems():
        
        for item in 
        driver.find_element_by_class_name ("tag-discount")
	     
    def test_find_many(self, driver)
        emptycart()
        driver.get("https://www.iceyarns.com/")
        Count= 19 # There are 19 items on the opening page + "Show More"
        noitems(Count)
        driver.find_element_by_class_name ("tag-discount").click()

        #form_element = driver.find_element_by_xpath("//form[@class='productcart']/input[1]").click()
        time.sleep(2) # Let the user actually see something!
        emptycart()
        driver.close()