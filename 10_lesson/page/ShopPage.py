import allure
from selenium.webdriver.common.by import By

@allure.epic("Магазин, страница выбора товара")
@allure.severity("blocker")

class ShopPage:
    
    @allure.id("Shop 2")
    @allure.title("Добавление товара")
    @allure.description("Добавление товара по условию задания")
    @allure.step("Добавление товара в корзину")
    def __init__(self, browser):
        self._browser = browser
    @allure.step("Добавление необходимого товара")
    def adding_product(self):
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()