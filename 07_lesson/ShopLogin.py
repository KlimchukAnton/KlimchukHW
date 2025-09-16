from selenium.webdriver.common.by import By

class ShopLogin:
    def __init__(self, browser):
        self._browser = browser
        self._browser.get("https://www.saucedemo.com/")
        self._browser.maximize_window()
        

    def login(self, login, password):
        self._browser.find_element(By.CSS_SELECTOR, "#user-name").clear()
        self._browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._browser.find_element(By.CSS_SELECTOR, "#password").clear()
        self._browser.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._browser.find_element(By.CSS_SELECTOR, "#login-button").click()
