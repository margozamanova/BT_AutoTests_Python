# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "File Upload"
# 4. Загрузите файл с картинкой
# 5. Нажмите на кнопку "Remove"
# 6. Загрузите пустой файл с расширением .txt (можно создать в блокноте)
# 7. Закройте появившееся красное сообщение об ошибке
# • Дополнительно(если получится): добавьте проверку что кнопка upload недоступна для нажатия


# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# 2. Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(20)

# 3. Перейдите в раздел "More" -> "File Upload"
More = driver.find_element_by_link_text("More")
More.click()
FileUpload = driver.find_element_by_css_selector("[href='FileUpload.html']")
FileUpload.click()
driver.execute_script("window.scrollBy(0, 300);")

# 4. Загрузите файл с картинкой
FotoUser = (r'C:\Users\CoRE\Desktop\LucasKing.png')
upload = driver.find_element_by_id("input-4")
upload.send_keys(FotoUser)

# 5. Нажмите на кнопку "Remove"
Remove_btn = driver.find_element_by_css_selector("[title='Clear selected files']")
Remove_btn.click()

# 6. Загрузите пустой файл с расширением .txt (можно создать в блокноте)
FileUser = (r'C:\Users\CoRE\Desktop\example.txt')
upload = driver.find_element_by_id("input-4")
upload.send_keys(FileUser)

# 7. Закройте появившееся красное сообщение об ошибке
ErrorClose_btn = driver.find_element_by_class_name("kv-error-close")
ErrorClose_btn.click()