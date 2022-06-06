# Shop: отображение, скидка товара
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)

# 1. Откройте http://practice.automationtesting.in/
import time
from selenium.webdriver.support.select import Select
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

# 4. Откройте книгу "Android Quick Start Guide"
android_quick_start_guide = driver.find_element_by_class_name('post-169')
android_quick_start_guide.click()

# 5. Добавьте тест, что содержимое старой цены = "₹600.00"
# используйте assert
OldPrice = driver.find_element_by_css_selector(".price > del > span")
OldPrice_text = OldPrice.text
assert OldPrice_text == "₹600.00"

# 6. Добавьте тест, что содержимое новой цены = "₹450.00"
# используйте assert
NewPrice = driver.find_element_by_css_selector(".price > ins > span")
NewPrice_text = NewPrice.text
assert NewPrice_text == "₹450.00"

# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
wait = WebDriverWait(driver, 10)
PictureView = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div > a")))
PictureView.click()

# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
PictureViewClose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
PictureViewClose.click()

driver.quit()
