# Shop: количество товаров в категории

# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара

# 1. Откройте http://practice.automationtesting.in/
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")

# 2. Залогиньтесь
# Нажмите на вкладку "My Account Menu"
MyAccount = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/my-account/']")
MyAccount.click()

# В разделе "Login", введите email для логина
# данные можно взять из предыдущего теста
UserName = driver.find_element_by_id("username")
UserName.send_keys("lucasking@gmail.com")

# В разделе "Login", введите пароль для логина
# данные можно взять из предыдущего теста
Password = driver.find_element_by_id("password")
Password.send_keys("p$9,zZcRg/kUzWW")

# Нажмите на кнопку "Login"
Login_btn = driver.find_element_by_css_selector("[value='Login']")
Login_btn.click()

# 3. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop.click()

# 4. Откройте категорию "HTML"
HTML_category = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']")
HTML_category.click()

# 5. Добавьте тест, что отображается три товара
BooksHTML = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cat-item-19 > span"), "3"))

driver.quit()