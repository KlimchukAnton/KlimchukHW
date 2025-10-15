import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.calcul_page import Calculpage
from page.calcul_operation import CalculOperation

@allure.epic("Работа калькулятора")
@allure.id("Calcul 1")
@allure.step("Настройка браузера Google Chrome через selenium")
def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calcul_page = Calculpage(browser)
    with allure.step("Выставление необходимого таймера получения результата, по условиям он составляет {second}сек."):
        calcul_page.data_entry("45")

 @allure.id("Calcul 2")
with allure.step("Вычисления выражения 7+8 через консоль"):
    calcul_operat = CalculOperation(browser)
    calcul_operat.operation()

@allure.id("Calcul 3")    
with allure.step("Проверка правильности работы калькулятора сравнением полученного из консоли результата с истинным значением"):
    assert calcul_operat.result() == "15"
with allure.step("Закрытие браузера командой Quit"):
    browser.quit