#Практическое задание: элементы

#1. Откройте https://opensource-demo.orangehrmlive.com
#2. Залогиньтесь и перейдите в PIM - > Employee List
#3. Нажмите на имя любого сотрудника (произойдёт переход в его карточку с данными)
#• если список пуст, создайте сотрудника вручную на этой же вкладке, нажав на"Add"
#4. Добавьте проверку, что радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора
#5. Добавьте проверку, что селектор Nationality в данный момент недоступен для выбора
#6. В карточке сотрудника, нажмите на кнопку "Edit"
#7. Измените пол сотрудника на противоположный
#8. Добавьте проверку, что радиокнопка с полом сотрудника действительно выбрана(атрибут появится после 12-го шага)
#9. В селекторе Nationality выберите самую последнюю страну в списке
#10. Добавьте проверку, что в селекторе Nationality выбрана последняя страна в списке(атрибут появится после 12-го шага)
#11. Выберите первоначальный пол сотрудника, а в селекторе Nationality выберите вариант "-- Select --"
#12. Сохраните изменения, нажав на кнопку "Save"

#1. Откройте https://opensource-demo.orangehrmlive.com
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/")

#2. Залогиньтесь и перейдите в PIM - > Employee List
login = driver.find_element_by_id("txtUsername")
login.send_keys("Admin")
password = driver.find_element_by_id("txtPassword")
password.send_keys("admin123")
login_btn = driver.find_element_by_id("btnLogin")
login_btn.click()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")

#3. Нажмите на имя любого сотрудника (произойдёт переход в его карточку с данными)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployee/empNumber/29")
# переходим в карточку сотрудника Charlie Carter

#4. Добавьте проверку, что радиокнопка с противоположным полом сотрудника в данный момент недоступна для выбора
gender_female = driver.find_element_by_id("personal_optGender_2")
gender_female_disabled = gender_female.get_attribute("disabled")
if gender_female_disabled is None:
    print("Check It! RadioButton Gender is available.")
else:
    print("Prohibited to change or choose employee Gender!")

#5. Добавьте проверку, что селектор Nationality в данный момент недоступен для выбора
empNation = driver.find_element_by_id("personal_cmbNation")
empNation_disabled = empNation.get_attribute("disabled")
if empNation_disabled is None:
    print("Change It! Selector Nationality is available.")
else:
    print("Prohibited to change employee Nationality!")

#6. В карточке сотрудника, нажмите на кнопку "Edit"
EditSave_btn = driver.find_element_by_id("btnSave")
EditSave_btn.click()
time.sleep(3)

#7. Измените пол сотрудника на противоположный
gender_female = driver.find_element_by_id("personal_optGender_2")
gender_female.click()
time.sleep(3)

#8. Добавьте проверку, что радиокнопка с полом сотрудника действительно выбрана(атрибут появится после 12-го шага)
gender_female_checked = gender_female.get_attribute("checked")
if gender_female_checked is not None:
    print("Radiobutton is checked!")
else:
    print("Please choose the gender for employee!")

#9. В селекторе Nationality выберите самую последнюю страну в списке
empNation = driver.find_element_by_id("personal_cmbNation")
empNation.click()
empNationLast = driver.find_element_by_css_selector("[value='193']")
empNationLast.click()
time.sleep(3)

#10. Добавьте проверку, что в селекторе Nationality выбрана последняя страна в списке(атрибут появится после 12-го шага)
empNationLast_checked = empNationLast.get_attribute("selected")
if empNationLast_checked is not None:
    print("Employee Nationality is selected!")
else:
    print("Please select the employee Nationality!")

#11. Выберите первоначальный пол сотрудника, а в селекторе Nationality выберите вариант "-- Select --"
gender_male = driver.find_element_by_id("personal_optGender_1")
gender_male.click()
empNation = driver.find_element_by_id("personal_cmbNation")
empNation.click()
empNationLast = driver.find_element_by_css_selector("[value='0']")
empNationLast.click()
time.sleep(3)

#12. Сохраните изменения, нажав на кнопку "Save"
EditSave_btn = driver.find_element_by_id("btnSave")
EditSave_btn.click()

driver.quit()