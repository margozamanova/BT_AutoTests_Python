# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html
# 2. Реализуйте неявное ожидание поиска элементов
# 3. Перейдите в раздел "More" -> "JQuery ProgressBar"
# 4. Реализуйте явное ожидание(EC) для проверки, что кнопка "Close" невидима
# • Для этого, предварительно вручную нажмите на кпоку "Start Download" и в появившемся окне возьмите селектор кнопки "Close"
# 5. Нажмите кнопку "Start Download"
# 6. Реализуйте явное ожидание(EC) для проверки, что кнопка называется "Cancel Download"
# 7. Закройте окно. Снова откройте
# 8. Реализуйте явное ожидание(EC) для проверки, что в окне присутствует текст "Complete!"


# 1. Откройте страницу: http://demo.automationtesting.in/WebTable.html

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver')
driver.maximize_window()

# 2. Реализуйте неявное ожидание поиска элементов
driver.implicitly_wait(5)
driver.get("http://demo.automationtesting.in/WebTable.html")

# 3. Перейдите в раздел "More" -> "JQuery ProgressBar"
More = driver.find_element_by_link_text("More")
More.click()
JQueryProgressBar = driver.find_element_by_css_selector("[href='JqueryProgressBar.html']")
JQueryProgressBar.click()

# 4. Реализуйте явное ожидание(EC) для проверки, что кнопка "Close" невидима
# • Для этого, предварительно вручную нажмите на кпопку "Start Download" и в появившемся окне возьмите селектор кнопки "Close"

wait = WebDriverWait(driver, 10)
Progress = wait.until(
EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ui-dialog-buttonset > button")))

# 5. Нажмите кнопку "Start Download"
StartDownload_btn = driver.find_element_by_id("downloadButton")
StartDownload_btn.click()

# 6. Реализуйте явное ожидание(EC) для проверки, что кнопка называется "Cancel Download"
Close = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".ui-dialog-buttonset > button"), "Cancel Download"))

# 7. Закройте окно. Снова откройте
Close_btn = driver.find_element_by_css_selector(".ui-dialog-buttonset > button")
Close_btn.click()
StartDownload_btn.click()

# 8. Реализуйте явное ожидание(EC) для проверки, что в окне присутствует текст "Complete!"
Complete_text = wait.until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".progress-label"), "Complete!"))

Close_btn = driver.find_element_by_css_selector(".ui-dialog-buttonset > button")
Close_btn.click()

driver.quit()