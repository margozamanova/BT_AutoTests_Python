# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "Switch to" -> "Windows"
# 4. В разделе "Open New Tabbed Windows" нажмите кнопку "click"
# 5. Переключите драйвер на вторую вкладку - > закройте её -> переключитесь обратно на первую вкладку
# • Чтобы закрыть вкладку: после переключения на неё на новой строке добавьте команду driver.close()
# 6. Перейдите в раздел "Separate Multiple Windows" и нажмите "click"
# 7. Переключите драйвер на вторую вкладку # здесь нужно будет использовать handles[2], тк ранее закрытая вкладка с шага 4 останется в
# памяти
# 8. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Index.html"
# 9. Используя явное ожидание(EC), проверьте что в браузере открыто 3 вкладки, выведите в консоли результат проверки (True/False)
# 10. В поле "email" напишите любую почту и нажмите на кнопку в виде ">" справа от поля
# 11. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Register.html"
# • Дополнительно(необязательно): для всех EC, вынесите часть проверки в переменную (как на последнем слайде перед практикой)

# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# 2. Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# 3. Перейдите в раздел "Switch to" -> "Windows"
SwitchTo = driver.find_element_by_css_selector("[href='SwitchTo.html']")
SwitchTo.click()
SwitchToWindows = driver.find_element_by_css_selector("[href='Windows.html']")
SwitchToWindows.click()
FirstTab = driver.current_window_handle

# 4. В разделе "Open New Tabbed Windows" нажмите кнопку "click"
TabbedClick_btn = driver.find_element_by_css_selector("[href='http://www.selenium.dev']")
TabbedClick_btn.click()

# 5. Переключите драйвер на вторую вкладку - > закройте её -> переключитесь обратно на первую вкладку
SecondTab = driver.window_handles[1]
driver.switch_to.window(SecondTab)
time.sleep(2)
driver.close()
driver.switch_to.window(FirstTab)
time.sleep(2)

# 6. Перейдите в раздел "Separate Multiple Windows" и нажмите "click"
SeparateMultipleWindows = driver.find_element_by_css_selector("li:nth-child(3) > a.analystic")
SeparateMultipleWindows.click()
time.sleep(2)
MultiClick_btn = driver.find_element_by_css_selector("[onclick='multiwindow()']")
MultiClick_btn.click()
time.sleep(2)

# 7. Переключите драйвер на вторую вкладку
# здесь нужно будет использовать handles[2], тк ранее закрытая вкладка с шага 4 останется в памяти
ThirdTab = driver.window_handles[2]
driver.switch_to.window(ThirdTab)

# 8. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Index.html"
wait = WebDriverWait(driver, 10)
link_check1 = wait.until(
EC.url_to_be("http://demo.automationtesting.in/Index.html"))

# 9. Используя явное ожидание(EC),
# проверьте что в браузере открыто 3 вкладки, выведите в консоли результат проверки (True/False)
OpenedTabsNumber = wait.until(EC.number_of_windows_to_be(3))
print(OpenedTabsNumber==3)

# 10. В поле "email" напишите любую почту и нажмите на кнопку в виде ">" справа от поля
EMail = driver.find_element_by_id("email")
EMail.send_keys("lucasking@gmail.com")
Enter_btn = driver.find_element_by_id("enterimg")
Enter_btn.click()

# 11. Используя явное ожидание(EC), проверьте что ссылка = "http://demo.automationtesting.in/Register.html"
# • Дополнительно(необязательно): для всех EC, вынесите часть проверки в переменную (как на последнем слайде перед практикой)
link_check2 = wait.until(
EC.url_to_be("http://demo.automationtesting.in/Register.html"))
