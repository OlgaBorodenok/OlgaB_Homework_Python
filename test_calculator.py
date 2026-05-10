from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # НОВЫЙ ИМПОРТ
from calculator_page import CalculatorPage


class TestCalculator:
    def setup_method(self):
        # Автоматически качает и подключает нужный драйвер
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.page = CalculatorPage(self.driver)

    def test_slow_calculator(self):
        self.page.open()
        self.page.set_delay("45")
        self.page.click_button("7")
        self.page.click_button("+")
        self.page.click_button("8")
        self.page.click_button("=")
        result = self.page.get_result()
        assert result == "15"

    def teardown_method(self):
        self.driver.quit()
