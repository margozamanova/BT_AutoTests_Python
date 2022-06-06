# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "Dynamic Data"
# • Здесь и в дальнейших заданиях используйте клики(их будет 2) вместо выбора по селектору
# 4. Добавьте проверку, что заголовок окна равен "Loading the data Dynamically"
# 5. Нажмите на кнопку "Get Dynamic Data"
# 6. Выведите в консоли адрес ссылки, которая сгенерируется в теге img (похожий на: https://randomuser.me/api/portraits/...)
# • Чтобы это сделать, используйте метод .get_attribute("атрибут")
# • Если адрес ссылки сильно отличается от примера в шаге 6, тогда после нажатия на кнопку из шага 5 добавьте паузу time.sleep(3)


# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# 2. Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)

# 3. Перейдите в раздел "More" -> "Dynamic Data"
More = driver.find_element_by_link_text("More")
More.click()
MoreLoader = driver.find_element_by_css_selector("[href='DynamicData.html']")
MoreLoader.click()

# 4. Добавьте проверку, что заголовок окна равен "Loading the data Dynamically"
WindowHead = driver.find_element_by_xpath("//div[@class='cont_box_center']/h3")
WindowHead_get_text = WindowHead.text
assert WindowHead_get_text == "Loading the data Dynamically"

# 5. Нажмите на кнопку "Get Dynamic Data"
GetDynamicData_btn = driver.find_element_by_id("save")
GetDynamicData_btn.click()

driver.quit()