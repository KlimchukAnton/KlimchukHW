from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

Inputs = driver.find_element(By.CSS_SELECTOR, "input")
Inputs.send_keys("Sky")

sleep(2)

Inputs.clear()

Inputs.send_keys("Pro")

sleep(2)

driver.quit()