from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def test_purchase():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    browser.maximize_window()
    
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.CSS_SELECTOR, "#user-name").clear()
    browser.find_element(
        By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    browser.find_element(By.CSS_SELECTOR, "#password").clear()
    browser.find_element(
        By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    browser.find_element(
        By.CSS_SELECTOR, "a.shopping_cart_link").click()
    browser.find_element(
        By.CSS_SELECTOR, "#checkout").click()
    
    browser.find_element(
        By.CSS_SELECTOR, "#first-name").send_keys("Ivan")
    browser.find_element(
        By.CSS_SELECTOR, "#last-name").send_keys("Petrov")
    browser.find_element(
        By.CSS_SELECTOR, "#postal-code").send_keys("562381")
    
    browser.find_element(
        By.CSS_SELECTOR, "#continue").click()
    
    total = browser.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text
    assert total == "Total: $58.29"
    print(total)
    
    browser.quit()