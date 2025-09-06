from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.fullscreen_window
browser.implicitly_wait(20)


browser.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

browser.find_element(By.CSS_SELECTOR, "#image-container")

src_atr = browser.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(src_atr)


browser.quit