from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from calcul_page import Calculpage
from calcul_operation import CalculOperation

def test_calculator():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calcul_page = Calculpage(browser)
    calcul_page.data_entry("45")
    
    calcul_operat = CalculOperation(browser)
    calcul_operat.operation()
    
    assert calcul_operat.result == "15"
    