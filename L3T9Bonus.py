# введение текста в модальное окно

import time
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

pageurl = 'https://www.google.com'
driver.get(pageurl)
driver.execute_script("alert('Hello dear!');")
time.sleep(5)

driver.quit()