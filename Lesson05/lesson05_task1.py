import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chromedriver_path = r'C:\Users\Comp1\.wdm\drivers\chromedriver\win64\109.0.5414.74\chromedriver.exe'

service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/classattr")

time.sleep(5)

try:
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.class3.btn-primary.btn-test")
except:
    try:
        blue_button = driver.find_element(By.XPATH, "//button[text()='Button Click']")
    except:
        try:
            blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        except:
            print("Не могу найти кнопку!")
            driver.quit()
            exit()

# Кликаем
blue_button.click()
print("Клик выполнен!")

time.sleep(3)

# Закрываем
driver.quit()
print("Готово")