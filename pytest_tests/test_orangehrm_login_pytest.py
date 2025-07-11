import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    yield driver, wait
    driver.quit()

def test_login_logout(setup_driver):
    driver, wait = setup_driver

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
    assert "login" in driver.current_url.lower()
