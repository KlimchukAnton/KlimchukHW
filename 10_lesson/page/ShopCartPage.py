from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import allure
from selenium.webdriver.common.by import By

@allure.epic("Магазин, корзина")
@allure.severity("blocker")

class ShopCartPage:

    @allure.id("Shop 3")
    @allure.title("Корзина магазина")
    @allure.description("Ввод необходимых данных для получения товара")
    def __init__(self, browser):
        self._browser = browser
    @allure.step("Переход на страницу корзины магазина")
    def get(self):
        with allure.step("Перейти в корзину магазина по ссылке"):
            self._browser.get("https://www.saucedemo.com/cart.html")
        with allure.step("Нажать кнопку"):
            self._browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    @allure.step("Ввод данных")
    def checkout_information(self, first_name, last_name, index):
        with allure.step("Ожидсние загрузки формы"):
            WebDriverWait(self._browser, 10).until(
                EC.presence_of_all_elements_located(By.CSS_SELECTOR, "#first-name"))
        with allure.step("Ввети имя"):
            self._browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        with allure.step("Ввести фамилию"):
            self._browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        with allure.step("Ввети индекс"):
            self._browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        with allure.step("Нажать кнопку Продолжить"):
            self._browser.find_element(By.CSS_SELECTOR, "#continue").click()
    @allure.step("Получить итоговую стоимость выбранных товаров")
    def total(self):
        total = self._browser.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        with allure.step("вернуть итоговую стоимость"):
            return total