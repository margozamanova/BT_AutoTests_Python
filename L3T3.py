# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Перейдите на вкладку "SwitchTo" - > "Alerts"
# • Здесь используйте клики(их будет 2) вместо выбора по селектору
# • Если не получится перейти на вкладку Alerts, тогда откройте страницу http://demo.automationtesting.in/Alerts.html и выполняйте задание начиная с 3-го шага
# 3. Нажмите на кнопку "click the button to display an alert box:" # перед нажатием добавьте паузу
# 4. Выведите в консоль содержимое окна alert и нажмите "OK"
# • Дополнительно(если получится): добавьте тест, что содержимое равно тексту "I am an alert box!" , а если не равно, тогда в консоли выводится сообщение об ошибке
# 5. Получите адрес текущей ссылки
# 6. Откройте новую вкладку в браузере, введите ссылку из предыдущего шага и перейдите по ней # перед открытием добавьте паузу
# 7. Нажмите на "Alert with OK & Cancel" -> "click the button to display a confirm box" # перед нажатием добавьте паузу
# 8. В модальном окне нажмите "Отмена"
# 9. Откройте новую вкладку в браузере, введите ссылку из шага 5 и перейдите по ней # перед открытием добавьте паузу
# 10. Нажмите на "Alert with Textbox"-> "click the button to demonstrate the prompt box" # перед нажатием добавьте паузу
# 11. В модальном окне, введите текст: "Ура! Задание выполнено!" и нажмите "OK"
# • Если вдруг никак не будет получаться переключаться между окнами браузера, выполните всё задание в одном окне
# • Если считаете, что селектор подобран правильно и почему-то не срабатывает, используйте между командами time.sleep(5)


# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
import time
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

driver.get("http://demo.automationtesting.in/WebTable.html")

# 2. Перейдите на вкладку "SwitchTo" - > "Alerts"
SwitchTo = driver.find_element_by_css_selector("[href='SwitchTo.html']")
SwitchTo.click()


SwitchToAlerts = driver.find_element_by_css_selector("[href='Alerts.html']")
SwitchToAlerts.click()

# 3. Нажмите на кнопку "click the button to display an alert box:"
# перед нажатием добавьте паузу
time.sleep(2)
AlertBox_btn = driver.find_element_by_id("OKTab")
AlertBox_btn.click()
time.sleep(2)

# 4. Выведите в консоль содержимое окна alert и нажмите "OK"
# • Дополнительно(если получится): добавьте тест, что содержимое равно тексту "I am an alert box!" ,
# а если не равно, тогда в консоли выводится сообщение об ошибке
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(2)
alert.accept()

if alert_text == "I am an alert box!":
    print("Good Job!")
else:
    print("ERROR!")

time.sleep(2)

# 5. Получите адрес текущей ссылки
currentPage = driver.current_url

# 6. Откройте новую вкладку в браузере, введите ссылку из предыдущего шага и
# перейдите по ней
# перед открытием добавьте паузу
driver.execute_script("window.open();")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.get(currentPage)

time.sleep(2)

# 7. Нажмите на "Alert with OK & Cancel" -> "click the button to display a confirm box"
# перед нажатием добавьте паузу
ConfirmOkCancel = driver.find_element_by_css_selector("[href='#CancelTab']")
ConfirmOkCancel.click()

time.sleep(2)

ConfirmBox_btn = driver.find_element_by_id("CancelTab")
ConfirmBox_btn.click()

# 8. В модальном окне нажмите "Отмена"
confirm = driver.switch_to.alert
confirm.dismiss()

time.sleep(2)

# 9. Откройте новую вкладку в браузере, введите ссылку из шага 5 и перейдите по ней
# перед открытием добавьте паузу
driver.execute_script("window.open();")
window_after = driver.window_handles[2]
driver.switch_to.window(window_after)
driver.get(currentPage)

# 10. Нажмите на "Alert with Textbox"-> "click the button to demonstrate the prompt box"
# перед нажатием добавьте паузу
time.sleep(2)
PromptTextbox = driver.find_element_by_css_selector("[href='#Textbox']")
PromptTextbox.click()

time.sleep(2)

# 11. В модальном окне, введите текст: "Ура! Задание выполнено!" и нажмите "OK"
PromptBox_btn = driver.find_element_by_id("Textbox")
PromptBox_btn.click()
prompt = driver.switch_to.alert
prompt.send_keys("Wooooww! I have done my homework!")
time.sleep(2)
prompt.accept()

time.sleep(2)
driver.quit()