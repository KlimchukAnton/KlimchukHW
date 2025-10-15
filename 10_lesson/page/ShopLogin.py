import allure
from selenium.webdriver.common.by import By

@allure.epic("Магазин, вход по логину и паролю")
@allure.severity("blocker")

class ShopLogin:
    
    @allure.id("Shop 1")
    @allure.title("Запуск браузера")
    @allure.description("Настройка браузера и переход на страницу магазина")
    @allure.step("Открытие страницы магазина с логином и паролем")
    def __init__(self, browser):
        self._browser = browser
        self._browser.get("https://www.saucedemo.com/")
        self._browser.maximize_window()
        
    @allure.title("Ввод логина и пароля")
    def login(self, login, password):
        with allure.step("Очитить поле user-name"):
            self._browser.find_element(By.CSS_SELECTOR, "#user-name").clear()
        with allure.step("Ввксти данные в поле user-name"):
            self._browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        with allure.step("Очистить поле password"):
            self._browser.find_element(By.CSS_SELECTOR, "#password").clear()
        with allure.step("Ввести данные в поле password"):
            self._browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        with allure.step("Нажать кнопку login"):
            self._browser.find_element(By.CSS_SELECTOR, "#login-button").click()
