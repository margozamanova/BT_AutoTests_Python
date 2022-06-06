# Откройте страницу https://opensource-demo.orangehrmlive.com/ и
# напишите тест для логина в систему



# 1. Открыть https://opensource-demo.orangehrmlive.com/
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# 2. Ввести Логин и пароль, зайти в систему
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")

password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")

login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
time.sleep(3)

# 3. Закрыть браузер
driver.quit()