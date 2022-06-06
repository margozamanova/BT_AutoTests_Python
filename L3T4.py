# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Перейдите в раздел "More" -> "Loader"
# 3. Реализуйте явное ожидание(EC) для отображения текста "Run"
# 4. Нажмите кнопку "Run"
# 5. Реализуйте явное ожидание(EC) что слово "Lorem" содержится в тексте модального окна
# 6. Реализуйте явное ожидание(EC) для нажатия в модальном окне на кнопку "Save Changes" и нажмите на неё


# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/WebTable.html")

# 2. Перейдите в раздел "More" -> "Loader"
More = driver.find_element_by_link_text("More")
More.click()
MoreLoader = driver.find_element_by_css_selector("[href='Loader.html']")
MoreLoader.click()

# 3. Реализуйте явное ожидание(EC) для отображения текста "Run"
wait = WebDriverWait(driver, 50)
run_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='loader']")))

# 4. Нажмите кнопку "Run"
driver.execute_script("window.scrollBy(0, 300);")
run_btn.click()

# 5. Реализуйте явное ожидание(EC) что слово "Lorem" содержится в тексте модального окна
MyModal = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='modal-body']/p"), str("Lorem")))

# 6. Реализуйте явное ожидание(EC) для нажатия в модальном окне на кнопку "Save Changes" и нажмите на неё
SaveChanges_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='history.go(0)']")))
SaveChanges_btn.click()

driver.quit()



