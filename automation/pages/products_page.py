from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_product = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.product_name = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        self.remove_product = (By.ID, "remove-sauce-labs-backpack")

    def add_backpack(self):
        self.driver.find_element(*self.add_product).click()

    def open_cart(self):
        self.driver.find_element(*self.cart).click()

    def get_product_name(self):
        self.product_name = self.driver.find_element(*self.product_name).text
        return self.product_name

    def remove_backpack(self):
        self.driver.find_element(*self.remove_product).click()