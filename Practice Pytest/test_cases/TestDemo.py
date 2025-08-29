import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_valid_login(setup):  # 'setup' param is the fixture injected here
    driver = setup
    driver.get("https://demo.nopcommerce.com/")
    driver.find_element(By.LINK_TEXT, "Log in").click()
    # continue test steps
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "nopCommerce")))


    assert "nopCommerce" in driver.title
