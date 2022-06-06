# Для сайта https://www.saucedemo.com/ напишите тест,
# в котором добавляется 3 товара в корзину и проверяется количество товаров в корзине

# 1. Открыть https://www.saucedemo.com/
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# 2. Ввести Логин и пароль, зайти в систему
username = driver.find_element_by_id("user-name")
username.send_keys("standard_user")

password = driver.find_element_by_id("password")
password.send_keys("secret_sauce")

login_btn = driver.find_element_by_id("login-button")
login_btn.click()

# 3. добавить в корзину 1-ый товар Sauce Labs Onesie
addSauceLabsOnesie_btn = driver.find_element_by_id("add-to-cart-sauce-labs-onesie")
addSauceLabsOnesie_btn.click()

# 4. добавить в корзину 2-ой товар Sauce Labs Fleece Jacket
addSauceLabsFleeceJacket_btn = driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket")
addSauceLabsFleeceJacket_btn.click()

# 5. добавить в корзину 3-й товар Sauce Labs Backpack
addSauceLabsBackpack_btn = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
addSauceLabsBackpack_btn.click()

# 6. Перейти в корзину
cart_btn = driver.find_element_by_id("shopping_cart_container")
cart_btn.click()
time.sleep(3)

# 7. Закрыть браузер
driver.quit()

