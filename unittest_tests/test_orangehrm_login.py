import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRMLoginLogoutDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 20)

    def test_login_logout(self):
        driver = self.driver
        wait = self.wait

        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field.send_keys('Admin')

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('admin123')

        login_button = driver.find_element(By.TAG_NAME, 'button')
        login_button.click()
        
        print("Login successful!")

        user_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-userdropdown-tab')))
        user_dropdown.click()

        logout_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout')))
        logout_link.click()

        print("Logout successful!")

        wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        self.assertIn("login", driver.current_url.lower())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
