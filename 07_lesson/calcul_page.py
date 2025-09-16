from selenium.webdriver.common.by import By

class Calculpage:
    def __init__(self, browser):
        self._browser = browser
        self._browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._browser.maximize_window()
        self._browser.implicitly_wait(46)

    def data_entry (self, number):
        self._browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(number)