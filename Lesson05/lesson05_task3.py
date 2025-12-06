import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

#путь к драйверу
GECKO_PATH = r"C:\Users\Comp1\AppData\Local\Programs\Python\Python38\Scripts\geckodriver.exe"

print(f"Используем драйвер: {GECKO_PATH}")

# Создаем сервис с указанием пути
service = Service(executable_path=GECKO_PATH)

# 1. Открыть браузер FireFox
print("Открываем Firefox...")
driver = webdriver.Firefox(service=service)

try:
    # 2. Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    print(f"Открыта страница: {driver.title}")
    time.sleep(2)
    
    # 3. Найти поле ввода (пробуем разные селекторы)
    try:
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    except:
        input_field = driver.find_element(By.TAG_NAME, "input")
    
    # 4. Ввести в поле текст Sky
    input_field.send_keys("Sky")
    print("Введено: Sky")
    time.sleep(1)
    
    # 5. Очистить это поле
    input_field.clear()
    print("Поле очищено")
    time.sleep(1)
    
    # 6. Ввести в поле текст Pro
    input_field.send_keys("Pro")
    print("Введено: Pro")
    time.sleep(2)
    
    print("\n" + "="*50)
    print("✅ ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ УСПЕШНО!")
    print("="*50)
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    
finally:
    # 7. Закрыть браузер
    driver.quit()
    print("Браузер закрыт")