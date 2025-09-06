from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.fullscreen_window


browser.get("http://uitestingplayground.com/textinput")

browser.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)
browser.quit