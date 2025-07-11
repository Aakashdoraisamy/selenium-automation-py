import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search(setup_driver):
    driver = setup_driver
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('leonardo dicaprio', Keys.RETURN)
    print("Search box found, value entered, and search submitted!")

    time.sleep(5)

    try:
        wiki_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Wikipedia')
        wiki_link.click()
        print("Wikipedia link clicked!")
    except Exception as e:
        print("Wikipedia link not found:", e)

    time.sleep(5)
