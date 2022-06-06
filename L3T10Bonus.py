# делаем скриншот страницы
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

pageurl = 'https://www.google.com'
driver.get(pageurl)
driver.save_screenshot("foto1")
time.sleep(2)

driver.quit()