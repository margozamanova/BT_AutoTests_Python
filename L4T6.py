# Shop: сортировка товаров
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value

# 1. Откройте http://practice.automationtesting.in/
import time
from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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

# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
OrderByDefault = driver.find_element_by_css_selector("[value='menu_order']")
OrderBy_checked = OrderByDefault.get_attribute("selected")
if OrderBy_checked is not None:
    print("Default Sorting is selected!")
else:
    print("Other type of Sorting is being used")

# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
OrderBy = driver.find_element_by_class_name("woocommerce-ordering")
OrderBy.click()
OrderByPriceDesc = driver.find_element_by_css_selector("[value='price-desc']")
OrderByPriceDesc.click()

# 6. Снова объявите переменную с локатором основного селектора сортировки
# т.к после сортировки страница обновится
OrderBy = driver.find_element_by_class_name("woocommerce-ordering")

# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
OrderByPriceDesc = driver.find_element_by_css_selector("[value='price-desc']")
OrderByPriceDesc_checked = OrderByPriceDesc.get_attribute("selected")
if OrderByPriceDesc_checked is not None:
    print("Sort by price: high to low is selected!")
else:
    print("Other type of Sorting is being used")

driver.quit()