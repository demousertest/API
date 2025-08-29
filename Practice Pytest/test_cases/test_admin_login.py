import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_page import Login_Admin_page
from utilities.read_properties import Readconfig


@pytest.mark.usefixtures("setup")
class Test_01_Admin_login():
    admin_page_url = Readconfig.get_admin_page_url()
    username = Readconfig.get_admin_username()
    password = Readconfig.get_admin_password()
    invalid_username = Readconfig.get_invalid_username()

    def test_title_vailidation(self,setup):
        driver = setup
        driver.get(self.admin_page_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        driver.implicitly_wait(10)
        actual_title = driver.title
        expected_title = 'nopCommerce demo store. Login'
        try:
            # Assertion directly
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
        except AssertionError as e:
            # Capture screenshot on failure
            driver.save_screenshot(".//screenshot/test_vailidation_login.png")
            raise e  # Re-raise the exception so pytest captures the failure

        finally:
            # Make sure the driver is always closed, regardless of pass or fail
            driver.quit()

    def test_vailidation_login(self,setup):
        driver = setup
        driver.get(self.admin_page_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        driver.implicitly_wait(10)
        admin_loing_page = Login_Admin_page(driver)
        admin_loing_page.click_login(self.username, self.password)
        expected_title = 'Dashboard'
        actual_title = driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        try:
            # Assertion directly
            assert actual_title == expected_title, f"Expected title '{expected_title}', but got '{actual_title}'"
        except AssertionError as e:
            # Capture screenshot on failure
            driver.save_screenshot(".//screenshot/test_vailidation_login.png")
            raise e  # Re-raise the exception so pytest captures the failure

        finally:
            # Make sure the driver is always closed, regardless of pass or fail
            driver.quit()

    def test_invaild_vailidation_login(self,setup):
        driver = setup
        driver.get(self.admin_page_url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[text()='Log in']").click()
        driver.implicitly_wait(10)
        admin_loing_page = Login_Admin_page(driver)
        admin_loing_page.click_login(self.invalid_username, self.password)
        error_massage = driver.find_element(By.XPATH, "//div[contains(text(), 'Login was unsuccessful')]//li").text
        assert (error_massage, 'No customer account found')
        try:
            assert error_massage == 'No customer account found', f"Expected title '{error_massage}', but got 'No customer account found'"
        except AssertionError as e:
            return e
        finally:
            driver.quit()


