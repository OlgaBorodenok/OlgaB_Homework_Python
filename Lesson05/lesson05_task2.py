import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

chromedriver_path = r'C:\Users\Comp1\.wdm\drivers\chromedriver\win64\109.0.5414.74\chromedriver.exe'

service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
time.sleep(1)

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

print(f"Кнопка нажата! ID кнопки: {button.get_attribute('id')}")

time.sleep(1)
driver.quit()
print("Готово")