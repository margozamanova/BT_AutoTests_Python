# Откройте страницу https://opensource-demo.orangehrmlive.com/
# и напишите тест для создания записи нового работника и ее удаления


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

# 5. Вернуться во вкладку Employee List и найти созданого пользователя
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")
EmpName = driver.find_element_by_id("empsearch_employee_name_empName")
time.sleep(3)
EmpName.send_keys("Lucas King")

search_btn = driver.find_element_by_id("searchBtn")
search_btn.click()

# 6. Отмечаем созданного пользователя в checkbox для удаления карточки пользователя
checkboxEmp_btn = driver.find_element_by_name("chkSelectRow[]")
checkboxEmp_btn.click()

delete_btn = driver.find_element_by_id("btnDelete")
delete_btn.click()

deleteOK_btn = driver.find_element_by_id("dialogDeleteBtn")
deleteOK_btn.click()

#должна появиться надпись зеленым цветом Successfully deleted
time.sleep(3)

# 7. Закрыть браузер
driver.quit()