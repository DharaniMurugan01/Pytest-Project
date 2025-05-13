import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('selenium locators')])
def test_google_search(search_term):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.co.in/")
    driver.find_element(By.NAME,"q").send_keys(search_term)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"gNO89b").click()
    time.sleep(6)
    driver.quit()