# Home: добавление комментария
#
# 1. Откройте http://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"

# 1. Откройте http://practice.automationtesting.in/
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")

# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
SeleniumRuby = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product/selenium-ruby/']")
SeleniumRuby.click()

# 4. Нажмите на вкладку "REVIEWS"
Reviews = driver.find_element_by_css_selector("[href='#tab-reviews']")
Reviews.click()
driver.execute_script("window.scrollBy(0, 600);")

# 5. Поставьте 5 звёзд
FiveStars = driver.find_element_by_class_name("star-5")
FiveStars.click()

# 6. Заполните поле "Review" сообщением: "Nice book!"
ReviewText = driver.find_element_by_id("comment")
ReviewText.send_keys("Nice book!")

# 7. Заполните поле "Name"
FirstName = driver.find_element_by_id("author")
FirstName.send_keys("Lucas")

# 8. Заполните "Email"
EMail = driver.find_element_by_id("email")
EMail.send_keys("lucasking@gmail.com")

# 9. Нажмите на кнопку "SUBMIT"
Submit_btn = driver.find_element_by_id("submit")
Submit_btn.click()

driver.quit()