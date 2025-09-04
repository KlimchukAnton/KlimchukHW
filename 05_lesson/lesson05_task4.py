from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

login = driver.find_element(By.CSS_SELECTOR, "#username")
login.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

login_click = driver.find_element(By.CSS_SELECTOR, "i.fa")
login_click.click()

secure_area = driver.find_element(By.CSS_SELECTOR, "#flash")
print(secure_area.text)

sleep(2)

driver.quit()