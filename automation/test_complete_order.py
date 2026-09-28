from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage

def test_complete_order(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack()

    products_page.open_cart()

    checkout_page.click_checkout()

    checkout_page.enter_checkout_info("Christos", "Christofi", "3050")

    checkout_page.click_continue()

    product_name = checkout_page.get_summary_product_name()
    assert "Sauce Labs Backpack" in product_name

    checkout_page.click_finish()

    confirmation_message = checkout_page.get_confirmation_message()
    assert "Thank you for your order!" in confirmation_message