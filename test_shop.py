import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    def _get_driver(self):
        """Возвращает настроенный драйвер Chrome"""
        # Если файл chromedriver.exe лежит в папке с тестом или в C:\webdriver
        local_driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

        if os.path.exists(local_driver_path):
            # Вариант 1: драйвер лежит рядом с тестом
            return webdriver.Chrome(service=Service(local_driver_path))
        elif os.path.exists(r"C:\webdriver\chromedriver.exe"):
            # Вариант 2: драйвер лежит в C:\webdriver (ваш случай)
            return webdriver.Chrome(service=Service(r"C:\webdriver\chromedriver.exe"))
        else:
            # Вариант 3: полагаемся на Selenium Manager (будет работать у преподавателя)
            return webdriver.Chrome()

    def test_total_price(self):
        driver = self._get_driver()
        driver.maximize_window()

        try:
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

            inventory_page = InventoryPage(driver)
            inventory_page.add_backpack()
            inventory_page.add_bolt_tshirt()
            inventory_page.add_onesie()

            inventory_page.go_to_cart()

            cart_page = CartPage(driver)
            cart_page.click_checkout()

            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form("Иван", "Петров", "101000")

            total = checkout_page.get_total()

            assert total == 58.29, f"Ожидалось 58.29, получено {total}"
        finally:
            driver.quit()