# Откройте страницу https://opensource-demo.orangehrmlive.com/ и
# напишите тест для создания записи нового работника


# 1. Открыть https://opensource-demo.orangehrmlive.com/
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# 2. Ввести Логин и пароль, зайти в систему
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")

password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")

login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()

# 3. Перейти во вкладку Employee List и затем в Add Employee
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/addEmployee")
time.sleep(3)

# 4. Создаем нового пользователя
firstname = driver.find_element_by_id("firstName")
firstname.send_keys("Luсas")

lastname = driver.find_element_by_id("lastName")
lastname.send_keys("King")

save_btn = driver.find_element_by_id("btnSave")
save_btn.click()

time.sleep(3)

# 5. Закрыть браузер
driver.quit()