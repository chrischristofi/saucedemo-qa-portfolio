from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"