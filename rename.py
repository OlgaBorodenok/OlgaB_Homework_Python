from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(5)

driver.get("http://uitestingplayground.com/textinput")

name_field = driver.find_element(By.ID, 'newButtonName')
name_field.send_keys('SkyPro')
        
blue_button = driver.find_element(By.ID, 'updatingButton')
blue_button.click()

import time
time.sleep(0.3)

button_text = blue_button.text
print(f"Текст кнопки: '{button_text}'")

driver.quit()