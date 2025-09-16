from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from ShopLogin import ShopLogin
from ShopPage import ShopPage
from ShopCartPage import ShopCartPage

def test_shop():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    shop_login = ShopLogin(browser)
    shop_login.login("standard_user", "secret_sauce")

    shop_page = ShopPage(browser)
    shop_page.adding_product()

    shop_cart = ShopCartPage(browser)
    shop_cart.get()
    shop_cart.checkout_nformation("Ivan", "Petrov", "858641")
    shop_cart.total()
    total = shop_cart.total()
    
    browser.quit
    assert total == "Total: $58.29"