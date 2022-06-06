# Registration_login: логин в систему
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"

# 1. Откройте http://practice.automationtesting.in/
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")

# 2. Нажмите на вкладку "My Account Menu"
MyAccount = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
MyAccount.click()

# 3. В разделе "Login", введите email для логина
# данные можно взять из предыдущего теста
UserName = driver.find_element_by_id("username")
UserName.send_keys("lucasking@gmail.com")

# 4. В разделе "Login", введите пароль для логина
# данные можно взять из предыдущего теста
Password = driver.find_element_by_id("password")
Password.send_keys("p$9,zZcRg/kUzWW")

# 5. Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']")
Login_btn.click()

# 6. Добавьте проверку, что на странице есть элемент "Logout"
Logout = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))

driver.quit()