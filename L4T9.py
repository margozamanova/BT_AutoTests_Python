# Shop: работа в корзине
#
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии

# 1. Откройте http://practice.automationtesting.in/
# в этом тесте логиниться не нужно
import time
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")

# 2. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop.click()

# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
HTML5_WebApp_Development_toCart = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5_WebApp_Development_toCart.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 600);")
JS_Data_Structures_and_Algorithm_toCart = driver.find_element_by_css_selector("[data-product_id='180']")
JS_Data_Structures_and_Algorithm_toCart.click()
time.sleep(5)

# 4. Перейдите в корзину
cart_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
time.sleep(5)

# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
remove_item = driver.find_element_by_css_selector("[data-product_id='182']")
remove_item.click()

# 6. Нажмите на Undo (отмена удаления)
Undo = driver.find_element_by_link_text("Undo?")
Undo.click()

# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()

Quantity_item = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
Quantity_item.clear()
time.sleep(5)
Quantity_item.send_keys(3)

# 8. Нажмите на кнопку "UPDATE BASKET"
Update_cart = driver.find_element_by_css_selector("[value='Update Busket']")
Update_cart.click()
time.sleep(5)

# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# используйте assert
Quantity_item = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
Quantity_item_value = Quantity_item.get_attribute("value")
assert Quantity_item_value == "3"
time.sleep(5)

# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
Apply_Coupon = driver.find_element_by_css_selector("[value='Apply Coupon']")
Apply_Coupon.click()
time.sleep(5)

# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
Coupon_message = driver.find_element_by_class_name("woocommerce-error")
Coupon_message_text = Coupon_message.text
print(Coupon_message_text == "Please enter a coupon code.")

driver.quit()

