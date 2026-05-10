from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.BOLT_TSHIRT_BTN = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.ONESIE_BTN = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        self.click(self.BACKPACK_BTN)

    def add_bolt_tshirt(self):
        self.click(self.BOLT_TSHIRT_BTN)

    def add_onesie(self):
        self.click(self.ONESIE_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)
