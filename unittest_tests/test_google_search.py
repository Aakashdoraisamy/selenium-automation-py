import unittest
import time  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchDemo(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        
    def test_search_box(self):
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('leonardo dicaprio', Keys.RETURN)
        print("Search box found, value entered, and search submitted!")
        time.sleep(15)  
        
        try:
            wiki_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Wikipedia')
            wiki_link.click()
            print("Wikipedia link clicked!")
        except Exception as e:
            print("Wikipedia link not found:", e)

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

