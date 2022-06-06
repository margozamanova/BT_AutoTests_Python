# получаем данные с сайта и делаем скриншот страницы
import time
from selenium import webdriver
from selenium.webdriver import Keys
from datetime import date
import datetime

driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

pageurl = 'https://www.google.com'
driver.get(pageurl)
search_field = driver.find_element_by_css_selector("input.gLFyf")
search_field.send_keys('weather tomorrow in Montreal Canada', Keys.ENTER)
time.sleep(2)
results = driver.find_element_by_xpath("//div[contains(text(), 'Результатов: примерно')]")
results_text = results.text
print(results_text)
results_number = ''.join([n for n in results_text if n.isdigit()])[:7]
print(results_number)
today = date.today()
tomorrow = today + datetime.timedelta(days=1)
print("For search request 'weather in Montreal Canada' " + str(results_number) + " results were found for " + str(tomorrow))
driver.save_screenshot(results_number + '.png')

driver.quit()





