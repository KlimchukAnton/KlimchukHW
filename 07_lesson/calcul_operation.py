from selenium.webdriver.common.by import By

class CalculOperation:
    def __init__(self, browser):
        self._browser = browser

    def operation(self):
        self._browser.find_element(By.XPATH, "//span[text()='7']").click()
        self._browser.find_element(By.XPATH, "//span[text()='+']").click()
        self._browser.find_element(By.XPATH, "//span[text()='8']").click()
        self._browser.find_element(By.XPATH, "//span[text()='=']").click()
        
    def result (self):
        txt = self._browser.find_element(By.CSS_SELECTOR, ".screen").text
        number_str = txt.split()[0]
        return int(number_str)