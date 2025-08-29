import time

from selenium.webdriver.common.by import By


class Login_Admin_page:
    username_id = 'Email'
    password_id = 'Password'
    login_button_id = "//button[@type='submit']"
    def __init__(self, driver):
        self.driver = driver

    def click_login(self, username, password):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.login_button_id).click()