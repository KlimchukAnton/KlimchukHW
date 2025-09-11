from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_calculator():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.implicitly_wait(46)
    
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    
    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()
    
    res = browser.find_element(By.CSS_SELECTOR, ".screen")
    assert res == "15"
    
    browser.quit()