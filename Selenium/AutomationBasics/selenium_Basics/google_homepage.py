from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service


browser = input('Enter the preferred browser name: ').lower()
match browser:
    case 'chrome':
        driver = webdriver.Chrome(service=Service("../resources/chromedriver.exe"))
        print('Chrome is opened successfully !!')
    case 'edge':
        driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))
        print('Edge opened successfully !!')
    case _:
        print('Select the CORRECT browser !')


driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(10)

driver.quit()