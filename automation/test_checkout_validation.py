from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

def test_checkout_validation(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack()

    products_page.open_cart()

    checkout_page.click_checkout()

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert "Error: First Name is required" in error_message