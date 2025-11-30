import allure
from selenium.webdriver.common.by import By

@allure.epic("Калькулятор")
@allure.severity("blocker")

class Calculpage:
    @allure.id("Calcul 1")
    @allure.title("Начало работы")
    @allure.description("Запуск браузера, настройка его, настройка таймера ожидания результата")
    @allure.step("Запуск браузера Google Chrome")
    def __init__(self, browser):
        self._browser = browser
        with allure.step("Переход на страницу калькулятора"):
            self._browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        with allure.step("Открытие окна браузера в полный экран"):
            self._browser.maximize_window()
        with allure.step("выставить таймер ожидание на 46сек., с помощью команды implicitly_wait"):
            self._browser.implicitly_wait(46)
    
    @allure.step("Работа с окном задержки результата")
    def data_entry (self, second):
        with allure.step("Очистка поля задержки"):
            self._browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        with allure.step("Команда установки задержки"):
            self._browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(second)