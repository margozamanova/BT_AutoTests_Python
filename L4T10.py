# Shop: покупка товара
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

# 1. Откройте http://practice.automationtesting.in/
# в этом тесте логиниться не нужно
import time
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
wait = WebDriverWait(driver, 10)

# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
Shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop.click()
driver.execute_script("window.scrollBy(0, 300);")

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
HTML5_WebApp_Development_toCart = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5_WebApp_Development_toCart.click()
time.sleep(5)

# 4. Перейдите в корзину
cart_btn = driver.find_element_by_class_name("wpmenucart-contents")
cart_btn.click()
time.sleep(5)

# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
Proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
Proceed_to_checkout.click()

# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# Данные для заполнения
# First Name: Lucas
# Last Name: King
# Email: LucasKing@gmail.com
# Cell Phone Number: +886905136457
# Country: Taiwan
# Address: 128 Sec. 2, Academia Road, Nankang
# Town: Taipei
# State: Taiwan
# Postcode: 115
#

FirstName = driver.find_element_by_id("billing_first_name")
FirstName.send_keys("Lucas")
LastName = driver.find_element_by_id("billing_last_name")
LastName.send_keys("King")
EMail = driver.find_element_by_id("billing_email")
EMail.send_keys("lucasking@gmail.com")
CellPhone = driver.find_element_by_id("billing_phone")
CellPhone.send_keys("+886905136457")
Country = driver.find_element_by_id("s2id_billing_country")
Country.click()
Country_user = driver.find_element_by_id("s2id_autogen1_search")
Country_user.send_keys("Taiwan")
Country_user_check = driver.find_element_by_id("select2-drop-mask")
# select2-choice
# select2-match
Country_user_check.click()
Address = driver.find_element_by_id("billing_address_1")
Address.send_keys("128 Sec. 2, Academia Road, Nankang")
Town = driver.find_element_by_id("billing_city")
Town.send_keys("Taipei")
State = driver.find_element_by_id("billing_state")
State.send_keys("Taiwan")
Postcode = driver.find_element_by_id("billing_postcode")
Postcode.send_keys("115")
time.sleep(5)

# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
Check_Payments = driver.find_element_by_id("payment_method_cheque")
Check_Payments.click()

# 8. Нажмите PLACE ORDER
Place_Order = driver.find_element_by_id("place_order")
Place_Order.click()

# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Order_window = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
Payment_Method_Order_window = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))

driver.quit()