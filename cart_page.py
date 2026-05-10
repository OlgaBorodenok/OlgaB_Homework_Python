from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CHECKOUT_BTN = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
