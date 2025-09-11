from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"C:\Users\user\Desktop\Python\Lesson6\msedgedriver.exe"
def test_form():
    browser = webdriver.Edge(service=EdgeService(edge_driver_path))
    browser.maximize_window()  
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    browser.find_element(
    By.CSS_SELECTOR, "[name=first-name]").send_keys("Иван")
    browser.find_element(
    By.CSS_SELECTOR, "[name=last-name]").send_keys("Петров")
    browser.find_element(
    By.CSS_SELECTOR, "[name=address]").send_keys("Ленина, 55-3")
    browser.find_element(
    By.CSS_SELECTOR, "[name=city]").send_keys("Москва")
    browser.find_element(
    By.CSS_SELECTOR, "[name=country]").send_keys("Россия")
    browser.find_element(
    By.CSS_SELECTOR, "[name=e-mail]").send_keys("test@skypro.com")
    browser.find_element(
    By.CSS_SELECTOR, "[name=phone]").send_keys("+7985899998787")
    browser.find_element(
    By.CSS_SELECTOR, "[name=job-position]").send_keys("QA")
    browser.find_element(
    By.CSS_SELECTOR, "[name=company]").send_keys("SkyPro")
    browser.find_element(
    By.CSS_SELECTOR, "[type=submit]").click()
    
    waiter = WebDriverWait(browser, 20)
    waiter.until(EC.presence_of_all_elements_located((
    By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
)
    
    zip_code = browser.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")
    
    green_field = browser.find_elements(By.CSS_SELECTOR, "div.alert-success")
    assert len(green_field) == 9
    
    browser.quit



# fields = ["first-name", "last-name", "address", "city", "country", "e_mail", "phone", "job_position", "company"]

# for field in fields:
#     color = browser.find_element(By.CSS_SELECTOR, ".form-label")
# color.value_of_css_property("background-color")

# assert zip_code == "#f8d7da"
# assert color == "#d1e7dd"

# browser.quit()