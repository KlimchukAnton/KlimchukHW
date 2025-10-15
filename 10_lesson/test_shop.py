import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from page.ShopLogin import ShopLogin
from page.ShopPage import ShopPage
from page.ShopCartPage import ShopCartPage

@allure.epic("Магазин")
@allure.severity("blocker")

@allure.epic("Магазин")

def test_shop():
    with allure.step("Запуск браузера"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    with allure.step("Войти по имеющимся данным")
        shop_login = ShopLogin(browser)
        shop_login.login("standard_user", "secret_sauce")
    
    with allure.step("Добавить товары в корзину"):
        shop_page = ShopPage(browser)
        shop_page.adding_product()

    with allure.step("Ввести данные получения"):
        shop_cart = ShopCartPage(browser)
        shop_cart.get()
        shop_cart.checkout_nformation("Ivan", "Petrov", "858641")
        shop_cart.total()
        total = shop_cart.total()
    with allure.step("Закрыть браузер командой quit"):
        browser.quit
    with allure.step("Выплнить проверку итоговой стоимости товаров с фактической, должны совпадать"):
        assert total == "Total: $58.29"