# 1. Настройте открытие окон в полный размер, с помощью команды из предыдущего урока: driver.maximize_window()
# • Для большей стабильности тестов, рекомендуется использовать её и в дальнейшем, указав сразу после инициализации драйвера: driver = webdriver.Chrome()
# 2. Откройте страницу http://demo.automationtesting.in/Register.html
# 3. Заполните произвольными данными только обязательные поля(*) в регистрации(а так же поля: Date of Birth, Password, Confirm Password)
# • Поле телефон должно содержать: 10 цифр, без +, например: 1234567890 ; если номер уже существует в системе – появится ошибка
# • Значение в селекторе country, date of birth выбирайте с помощью класса Select из библиотеки WebDriver
# • Если будет отображаться селектор "country", состоящий из 1-го варианта, тогда его можно не заполнять, и также можно пропустить 7-й пункт этого задания
# • Поля password, confirm password должны содержать: не менее 6 символов, маленькую букву, большую букву, цифру
# 4. Загрузите любой файл в раздел "Photo" вверху справа
# 5. Проскролльте страницу вниз на 300 пикселей
# 6. Нажмите на кнопку Submit # если будет селектор "country", состоящий из 1-го варианта, тогда кнопка не нажмется, в таком варианте будет окей. Просто добавьте код для её нажатия.
# 7. Добавьте проверку, что произошёл переход на страницу: http://demo.automationtesting.in/WebTable.html
# • Дополнительно: улучшите проверку таким образом, чтобы в консоли выводилось содержательное сообщение, из которого можно понять, на какой странице находимся
# сейчас и на какой странице ожидаем находиться.
# • Не забывайте использовать time.sleep() если нужно
# • В задании можно иногда использовать XPATH (пример структуры: //тег[@атрибут='значение']
# • Будет также полезно вспомнить про составной селектор (пример структуры: .class .other class) ; (пример структуры 2: #someid .someclass)
# • Ещё здесь может пригодиться nth-child() (пример структуры: element:nth-child(порядковый номер)


#1. import time, import webdriver, import Select, maximize_window

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

#2. Откройте страницу http://demo.automationtesting.in/Register.html

driver.get("http://demo.automationtesting.in/Register.html")

#3. Заполните произвольными данными только обязательные поля(*) в регистрации(а так же поля: Date of Birth, Password, Confirm Password)
# Date of Birth: 06.09.2000
# Password: qweRt28
# Confirm Password: qweRt28
# Cell phone 89627829516
# *Full Name: Lucas King (First Name Lucas, Last Name King)
# *Email address: lucasking@gmail.com
# *Gender: Male
# Country: no options to choose

FirstName = driver.find_element_by_css_selector("[placeholder='First Name']")
FirstName.send_keys("Lucas")
LastName = driver.find_element_by_css_selector("[placeholder='Last Name']")
LastName.send_keys("King")
EMail = driver.find_element_by_css_selector("[type='email']")
EMail.send_keys("lucasking@gmail.com")
CellPhone = driver.find_element_by_css_selector("[type='tel']")
CellPhone.send_keys("9627829516")
genderMale = driver.find_element_by_css_selector("[value='Male']")
genderMale.click()

time.sleep(2)

YYYYUser = driver.find_element_by_id("yearbox")
select = Select(YYYYUser)
select.select_by_visible_text("2000")
MMUser = driver.find_element_by_css_selector("[placeholder='Month']")
select = Select(MMUser)
select.select_by_value("September")
DDUser = driver.find_element_by_id("daybox")
select = Select(DDUser)
select.select_by_value("6")
time.sleep(2)

Password = driver.find_element_by_id("firstpassword")
Password.send_keys("qweRt28")
PasswordProve = driver.find_element_by_id("secondpassword")
PasswordProve.send_keys("qweRt28")
time.sleep(2)

#4. Загрузите любой файл в раздел "Photo" вверху справа

FotoUser = (r'C:\Users\CoRE\Desktop\LucasKing.png')
upload = driver.find_element_by_id("imagesrc")
upload.send_keys(FotoUser)
time.sleep(2)

#5. Проскролльте страницу вниз на 300 пикселей

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

#6. Нажмите на кнопку Submit
# если будет селектор "country", состоящий из 1-го варианта, тогда кнопка не нажмется, в таком варианте будет окей. Просто добавьте код для её нажатия.

#Country = driver.find_element_by_id("countries")
#Country.click()
#CountryUser = driver.find_element_by_css_selector("[value='Select Country']")
#CountryUser.click()

Submit_btn = driver.find_element_by_id("submitbtn")
Submit_btn.click()

#7. Добавьте проверку, что произошёл переход на страницу: http://demo.automationtesting.in/WebTable.html
#• Дополнительно: улучшите проверку таким образом, чтобы в консоли выводилось содержательное сообщение, из которого можно понять, на какой странице находимся
#сейчас и на какой странице ожидаем находиться.

currentPage = driver.current_url
expectedPage = "http://demo.automationtesting.in/WebTable.html"
if currentPage == expectedPage:
    print("Match")
    driver.execute_script("alert('Registration completed successfully!');")
else:
    print("Not Match, current page:"+ currentPage)
    print("Expected page:" + expectedPage)
    driver.execute_script("alert('Please complete the registration form');")
    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

time.sleep(2)
driver.quit()