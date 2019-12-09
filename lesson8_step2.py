from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    browser.find_element_by_css_selector("button.btn").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element_by_id("input_value")
    y = calc(x_element.text)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector("button#solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()