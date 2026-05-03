import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()


driver.get("https://www.google.com")

print("Opened Google successfully")
time.sleep(10)
driver.maximize_window()
driver.quit()

'''
assert "Google" in driver.title
print("Title Test Passed")

search_box = driver.find_element(By.NAME, "q")
assert search_box.is_displayed()
print("Search Box Test Passed")

search_box.send_keys("Selenium Testing")
print("Text Entered Successfully")'''

