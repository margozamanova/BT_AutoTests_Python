# Registration_login: регистрация аккаунта
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"

# 1. Откройте http://practice.automationtesting.in/
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")

# 2. Нажмите на вкладку "My Account Menu"
MyAccount = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
MyAccount.click()

# 3. В разделе "Register", введите email для регистрации
EMail = driver.find_element_by_id("reg_email")
EMail.send_keys("lucasking@gmail.com")

# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
Password = driver.find_element_by_id("reg_password")
Password.send_keys("p$9,zZcRg/kUzWW")

# 5. Нажмите на кнопку "Register"
Register_btn = driver.find_element_by_css_selector("[value='Register']")
Register_btn.click()

driver.quit()