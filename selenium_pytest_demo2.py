import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()

def test_login(driver):
    driver.get("https://trytestingthis.netlify.app/index.html")
    driver.find_element(By.ID,"uname").send_keys("test")
    driver.find_element(By.ID, "pwd").send_keys("test")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()

    assert "Successful" in driver.page_source

