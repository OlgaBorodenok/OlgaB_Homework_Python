import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Путь к драйверу
GECKO_PATH = r"C:\Users\Comp1\AppData\Local\Programs\Python\Python38\Scripts\geckodriver.exe"

print(f"Используем драйвер: {GECKO_PATH}")

service = Service(executable_path=GECKO_PATH)

print("Открываем Firefox...")
driver = webdriver.Firefox(service=service)

try:
    print("Переходим на страницу входа...")
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)
    
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("Введен username: tomsmith")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введен password: SuperSecretPassword!")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Нажата кнопка Login")
    time.sleep(2)
    
    flash_message = driver.find_element(By.ID, "flash")
    flash_text = flash_message.text.strip()
    print("\n" + "="*50)
    print("Текст с зеленой плашки:")
    print(flash_text)
    print("="*50)
    
    time.sleep(2)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    print("\nЗакрываем браузер...")
    driver.quit()