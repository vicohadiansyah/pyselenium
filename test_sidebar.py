import unittest


import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()

class TestSidebar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://xdmin199x:twMydn1AtRpJHlELvnvd@staging-dashboard.skul.id/admin")
        self.driver.set_window_size(974, 1032)

    def tearDown(self):
        self.driver.quit()

    def test_expandsidebar(self):
        driver = self.driver
        driver.find_element(By.NAME, "email").send_keys("admin@skul.id")
        driver.find_element(By.NAME, "password").send_keys("Iniq6jxx3sxeGxcbPhhjdf4rm")
        driver.find_element(By.XPATH, "(//button[normalize-space()='LOGIN'])[1]").click()
        time.sleep(2)
        assert "Selamat datang di dashboard skul.id" in driver.page_source

        sidebar_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[@class='header-toggler class-toggler mfs-3 d-md-down d-lg-none'])[1]"))
        )
        self.assertTrue(sidebar_element.is_enabled())
        sidebar_element.click()
        time.sleep(2)



