from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text):
        xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        # Ждём, пока в результате исчезнет знак +
        self.wait.until(
            lambda d: "+" not in d.find_element(By.CSS_SELECTOR, ".screen").text
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
