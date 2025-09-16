from selenium.webdriver.common.by import By

class ShopCartPage:
    def __init__(self, browser):
        self._browser = browser

    def get(self):
        self._browser.get("https://www.saucedemo.com/cart.html")
        self._browser.find_element(By.CSS_SELECTOR, "#checkout").click()

    def checkout_nformation(self, first_name, last_name, index):
        self._browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(index)
        self._browser.find_element(By.CSS_SELECTOR, "#continue").click()

    def total(self):
        total = browser.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        print(total)