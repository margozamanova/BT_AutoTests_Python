# Shop: проверка цены в корзине
#
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
#
# # если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# # если все книги будут out of stock - тогда пропустите это и следующие два задания

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

# 2. Нажмите на вкладку "Shop"
Shop = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/shop/']")
Shop.click()

# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
HTML5_WebApp_Development_toCart = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5_WebApp_Development_toCart.click()
time.sleep(5)

# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert

cart_items = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
cart_items_text = cart_items.text
assert cart_items_text == "1 Item"

cart_total_price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
cart_total_price_text = cart_total_price.text
assert cart_total_price_text == "₹180.00"

# 5. Перейдите в корзину
cart_btn = driver.find_element_by_css_selector(".wpmenucart-contents")
cart_btn.click()
time.sleep(5)

# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
wait = WebDriverWait(driver, 20)
Subtotal_cart = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), str("₹180.00")))

# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
Total_cart = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), str("₹189.00")))

driver.quit()



