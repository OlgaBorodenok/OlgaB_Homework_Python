import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

BROWSER_TO_USE = "chrome"

# ВНИМАНИЕ: Из-за технических ограничений Windows 7 (Edge 109 не имеет драйвера)
# тест выполняется на Chrome. Для проверки на Edge достаточно изменить:
# BROWSER_TO_USE = "chrome"  →  BROWSER_TO_USE = "edge"

CHROME_DRIVER_PATH = r'C:\webdriver\chromedriver.exe'

class TestShop:
    """Тест для проверки покупки на сайте saucedemo.com"""
    
    def get_driver(self):
        
        if BROWSER_TO_USE.lower() == "chrome":
            print(f"Используется Chrome (путь: {CHROME_DRIVER_PATH})")
            service = ChromeService(executable_path=CHROME_DRIVER_PATH)
            driver = webdriver.Chrome(service=service)
            
        elif BROWSER_TO_USE.lower() == "edge":
            print(f"Используется Edge (путь: {EDGE_DRIVER_PATH})")
            service = EdgeService(executable_path=EDGE_DRIVER_PATH)
            driver = webdriver.Edge(service=service)
            
        else:
            raise ValueError(f"Неподдерживаемый браузер: {BROWSER_TO_USE}")
        
        driver.maximize_window()
        return driver
    
    def test_shop_purchase(self):
        """
        Основной тест покупки
        Использует браузер, указанный в настройке BROWSER_TO_USE
        """
        driver = self.get_driver()
        
        try:
            # Шаг 1: Открыть сайт
            print("\n" + "=" * 60)
            print(f"ШАГ 1: Открываем сайт saucedemo.com в {BROWSER_TO_USE}")
            print("=" * 60)
            driver.get("https://www.saucedemo.com/")
            
            # Создаем объект WebDriverWait для ожиданий
            wait = WebDriverWait(driver, 10)
            
            # Шаг 2: Авторизация
            print("\nШАГ 2: Авторизуемся как standard_user")
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            username_field.send_keys("standard_user")
            
            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys("secret_sauce")
            
            login_button = driver.find_element(By.ID, "login-button")
            login_button.click()
            print("✓ Авторизация выполнена")
            
            # Шаг 3: Добавление товаров в корзину
            print("\nШАГ 3: Добавляем товары в корзину")
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
            )
            
            # Список товаров для добавления
            items_to_add = [
                ("add-to-cart-sauce-labs-backpack", "Sauce Labs Backpack"),
                ("add-to-cart-sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"),
                ("add-to-cart-sauce-labs-onesie", "Sauce Labs Onesie")
            ]
            
            for item_id, item_name in items_to_add:
                item_button = wait.until(
                    EC.element_to_be_clickable((By.ID, item_id))
                )
                item_button.click()
                print(f"  ✓ Добавлен: {item_name}")
            
            # Шаг 4: Переход в корзину
            print("\nШАГ 4: Переходим в корзину")
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
            )
            cart_icon.click()
            print("✓ Перешли в корзину")
            
            # Шаг 5: Нажатие Checkout
            print("\nШАГ 5: Нажимаем Checkout")
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
            print("✓ Нажали Checkout")
            
            # Шаг 6: Заполнение формы
            print("\nШАГ 6: Заполняем форму данными")
            wait.until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            
            first_name_field = driver.find_element(By.ID, "first-name")
            first_name_field.send_keys("Ольга")
            
            last_name_field = driver.find_element(By.ID, "last-name")
            last_name_field.send_keys("Бороденок")
            
            postal_code_field = driver.find_element(By.ID, "postal-code")
            postal_code_field.send_keys("454028")
            print("  ✓ Имя: Ольга")
            print("  ✓ Фамилия: Бороденок")
            print("  ✓ Индекс: 454028")
            
            # Шаг 7: Нажатие Continue
            print("\nШАГ 7: Нажимаем Continue")
            continue_button = driver.find_element(By.ID, "continue")
            continue_button.click()
            print("✓ Нажали Continue")
            
            # Шаг 8: Чтение итоговой стоимости
            print("\nШАГ 8: Читаем итоговую стоимость")
            total_label = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
            )
            total_text = total_label.text
            total_value = total_text.replace("Total: ", "").strip()
            
            print(f"  ✓ Получена итоговая сумма: {total_value}")
            
            # Шаг 9: Проверка итоговой суммы
            print("\nШАГ 9: Проверяем соответствие ожидаемой сумме")
            expected_total = "$58.29"
            assert total_value == expected_total, \
                f"Ожидалась сумма {expected_total}, получена {total_value}"
            
            print(f"\n{'=' * 60}")
            print(f"✅ ТЕСТ УСПЕШНО ПРОЙДЕН НА {BROWSER_TO_USE.upper()}!")
            print(f"Итоговая сумма: {total_value} соответствует ожидаемой {expected_total}")
            print(f"{'=' * 60}")
            
        except Exception as e:
            # В случае ошибки делаем скриншот
            screenshot_path = f"error_screenshot_{BROWSER_TO_USE}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n❌ ПРОИЗОШЛА ОШИБКА: {str(e)}")
            print(f"Скриншот сохранен: {screenshot_path}")
            raise e
        
        finally:
            # Шаг 10: Закрытие браузера
            print("\nШАГ 10: Закрываем браузер")
            driver.quit()
            print("✓ Браузер закрыт")

#pytest test_03_shop.py -v -s
