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

def test_expandsidebar(driver):
    driver.get("https:///xdmin199x:twMydn1AtRpJHlELvnvd@staging-dashboard.skul.id/admin")
    driver.set_window_size(974, 1032)
    driver.find_element(By.NAME, "email").send_keys("admin@skul.id")
    driver.find_element(By.NAME, "password").send_keys("Iniq6jxx3sxeGxcbPhhjdf4rm")
    driver.find_element(By.XPATH, "(//button[normalize-space()='LOGIN'])[1]").click()
    time.sleep(2)
    assert "Selamat datang di dashboard skul.id" in driver.page_source
    driver.find_element(By.XPATH, "//div[@class='row']//div[1]//div[1]//div[3]").click()

