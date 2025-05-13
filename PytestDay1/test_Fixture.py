import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(params=[("chrome", "https://tutorialsninja.com/demo/"), 
                        ("edge", "https://tutorialsninja.com/demo/")])
def setup(request):
    browser, url = request.param
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        pytest.skip("Unsupported browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    yield driver  
    driver.quit()
def test_validsearch(setup):
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("Hp")
    driver.find_element(By.XPATH, "//i[@class='fa fa-search']").click()
    assert driver.find_element(By.XPATH, "//div[@id='content']/child::h1").text == "Search - Hp"
def test_Invalidsearch(setup):
    driver = setup
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("")
    driver.find_element(By.XPATH, "//i[@class='fa fa-search']").click()
    text1 = driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::h2").text
    assert text1 == "Products meeting the search criteria"
def test_emptysearch(setup):
    driver=setup
    driver.find_element(By.XPATH, "//input[@name='search']").send_keys("Honda")
    driver.find_element(By.XPATH, "//i[@class='fa fa-search']").click()
    text2=driver.find_element(By.XPATH,"(//input[@id='button-search']/following::p)[1]").text
    assert text2=="There is no product that matches the search criteria."