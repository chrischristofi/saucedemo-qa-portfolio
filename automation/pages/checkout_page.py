from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout = (By.ID, "checkout")
        self.continue_checkout = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.summary_product_name = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
        self.finish = (By.ID, "finish")
        self.confirmation_message = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout)
        ).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_checkout).click()

    def get_error_message(self):
        self.error_message = self.driver.find_element(*self.error_message).text
        return self.error_message

    def enter_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def get_summary_product_name(self):
        product_name = self.driver.find_element(*self.summary_product_name).text
        return product_name

    def click_finish(self):
        self.driver.find_element(*self.finish).click()

    def get_confirmation_message(self):
        confirmation_message = self.driver.find_element(*self.confirmation_message).text
        return confirmation_message