import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для Chrome (рабочий вариант)
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Для Edge (закомментировано, но готово к использованию)
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.edge.options import Options as EdgeOptions

class TestSlowCalculator:
    
    def test_slow_calculator(self):
        # Настройка для Chrome
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        
        # Путь к ChromeDriver
        chrome_driver_path = r'C:\webdriver\chromedriver.exe'
        
        # Создаем сервис для Chrome
        chrome_service = ChromeService(executable_path=chrome_driver_path)
        
        # Создаем драйвер Chrome
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        try:
            # Шаг 1: Открыть страницу
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            
            # Шаг 2: Ввести значение 45
            delay_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
            )
            delay_input.clear()
            delay_input.send_keys("45")
            
            # Шаг 3: Нажать на кнопки
            buttons_to_click = ["7", "+", "8", "="]
            
            for button_text in buttons_to_click:
                button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
                )
                button.click()
            
            # Шаг 4: Проверить результат
            WebDriverWait(driver, 50).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
            )
            
            actual_result = driver.find_element(By.CSS_SELECTOR, ".screen").text
            assert actual_result == "15", f"Ожидалось 15, но получено {actual_result}"
            
        finally:
            driver.quit()


# запуск: pytest test_02_calc.py -v