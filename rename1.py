from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
    
name_field = driver.find_element(By.ID, 'newButtonName')
name_field.send_keys('SkyPro')
    
blue_button = driver.find_element(By.ID, 'updatingButton')
blue_button.click()
    
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.ID, 'updatingButton'), 'SkyPro'))

blue_button = driver.find_element(By.ID, 'updatingButton')
button_text = blue_button.text
print(f"Текст кнопки: '{button_text}'")
    
if button_text == 'SkyPro':
    print("Успех: кнопка переименована корректно!")
else:
    print(f"Ошибка: ожидался текст 'SkyPro', получен '{button_text}'")

driver.quit()