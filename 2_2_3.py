import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//div[@class = 'form-group']//input[1]")
    input1.send_keys("Zahoder")
    input2 = browser.find_element(By.XPATH, "//div[@class = 'form-group']//input[2]")
    input2.send_keys("Zakharyanskiy")
    input3 = browser.find_element(By.XPATH, "//div[@class = 'form-group']//input[3]")
    input3.send_keys("Zahoder@007")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "button.btn.btn-primary")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()