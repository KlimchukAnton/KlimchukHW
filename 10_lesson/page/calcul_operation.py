import allure
from selenium.webdriver.common.by import By

@allure.epic("Калькулятор, консоль для операций")
@allure.severity("blocker")

class CalculOperation:
    @allure.id("Calcul 2")
    @allure.title("Консоль операций")
    @allure.description("Произвести вычесления с поиощью консоли")
    def __init__(self, browser):
        self._browser = browser
    @allure.step("Работа с консолью калькулятора")
    def operation(self):
        with allure.step("Нажать кнопку 7"):
            self._browser.find_element(By.XPATH, "//span[text()='7']").click()
        with allure.step("Нажать кнопку +"):
            self._browser.find_element(By.XPATH, "//span[text()='+']").click()
        with allure.step("Нажать кнопку 8"):
            self._browser.find_element(By.XPATH, "//span[text()='8']").click()
        with allure.step("Нажать кнопку ="):
            self._browser.find_element(By.XPATH, "//span[text()='=']").click()
    
    @allure.step("Возвращение результата")
    def result (self):
        with allure.step("Преобразование результата в текст"):
            txt = self._browser.find_element(By.CSS_SELECTOR, ".screen").text
        with allure.step("Присвоение переменной для результата"):
            number_str = txt.split()[0]
        with allure.step("Возвращение переобразованной переменной"):
            return int(number_str)