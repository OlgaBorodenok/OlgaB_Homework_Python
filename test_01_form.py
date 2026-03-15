import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os

def test_data_types_form():
    """
    Тест для проверки подсветки полей формы после отправки
    """
    # Путь к ChromeDriver
    driver_path = r'C:\webdriver\chromedriver.exe'
    
# для Edge меняем driver = webdriver.Chrome(service=service) НА driver = webdriver.Edge(service=Service(r'C:\webdriver\msedgedriver.exe'))

    # Проверяем, существует ли файл
    if not os.path.exists(driver_path):
        print("\n" + "="*50)
        print("⚠️  ДРАЙВЕР НЕ НАЙДЕН!")
        print("="*50)
        print(f"Скачай ChromeDriver и положи сюда: {driver_path}")
        print("="*50 + "\n")
        pytest.fail(f"Драйвер не найден!")
    
    # Создаем сервис с указанием пути к драйверу
    service = Service(executable_path=driver_path)
    
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    try:
        # Шаг 1: Открыть страницу
        print("Открываем страницу...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        
        # Ожидание загрузки формы
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        
        # Шаг 2: Заполнение формы
        print("Заполняем форму...")
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        
        for field_name, value in form_data.items():
            field = driver.find_element(By.NAME, field_name)
            field.clear()
            field.send_keys(value)
        
        # Шаг 3: Нажать кнопку Submit
        print("Отправляем форму...")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Шаг 4: Ожидание подсветки полей
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success, .alert-danger")))
        
        # Шаг 5: Проверка подсветки
        print("Проверяем подсветку полей...")
        
        # Zip code должен быть красным
        zip_code = driver.find_element(By.ID, "zip-code")
        zip_class = zip_code.get_attribute("class")
        assert "danger" in zip_class, f"Zip code должен быть красным"
        print("✅ Zip code красный")
        
        # Остальные поля должны быть зелеными
        green_fields = ["first-name", "last-name", "address", "e-mail", 
                       "phone", "city", "country", "job-position", "company"]
        
        for field_id in green_fields:
            field = driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert "success" in field_class, f"Поле {field_id} должно быть зеленым"
            print(f"✅ {field_id} зеленый")
        
        print("\n" + "="*50)
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        driver.save_screenshot("error.png")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

    # запуск:  pytest test_01_form.py -v -s