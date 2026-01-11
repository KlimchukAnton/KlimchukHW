from selenium.webdriver.common.by import By

class ShopPage:
    
    def __init__(self, browser):
        self._browser = browser

    def adding_product(self):
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()