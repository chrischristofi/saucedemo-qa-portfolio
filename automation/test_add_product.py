from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_add_product(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack()

    cart_count = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']").text
    assert "1" in cart_count

    products_page.open_cart()

    product_name = products_page.get_product_name()
    assert "Sauce Labs Backpack" in product_name

    products_page.remove_backpack()

    product = driver.find_elements(By.CSS_SELECTOR, "[data-test='cart-item']")
    assert len(product) == 0