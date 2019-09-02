from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://python.org')
time.sleep(2) # Let the user actually see something!
driver.quit()