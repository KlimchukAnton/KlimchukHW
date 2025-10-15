import allure
from selenium.webdriver.common.by import By

class Calculpage:
    @allure.step("Запуск браузера Google Chrome и выставление настроек")
    def __init__(self, browser):
        self._browser = browser
        with allure.step("Переход на страницу калькулятора"):
            self._browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        with allure.step("Открытие окна браузера в полный экран"):
            self._browser.maximize_window()
        with allure.step("выставить таймер ожидание на 46сек. с помощью команды implicitly_wait"):
            self._browser.implicitly_wait(46)
    @allure.step("Работа с окном задержки результата")
    def data_entry (self, second):
        with allure.step("Очистка поля задержки"):
            self._browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        with allure.step("Команда установки задержки"):
            self._browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(second)