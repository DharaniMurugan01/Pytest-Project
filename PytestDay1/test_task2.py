import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("browser,url", [
    ("chrome", "https://www.flipkart.com/"),
    ("chrome", "https://www.amazon.in/"),
    ("firefox", "https://www.flipkart.com/"),
    ("firefox", "https://www.amazon.in/")
])

def test_browser(browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.maximize_window()
    driver.get(url)
    print(driver.title)
    time.sleep(2)
    driver.quit()
