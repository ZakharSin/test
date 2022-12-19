from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "  http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.form-group.second_class [type="text"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//div/form/div[1]/div[3]/input')
    input3.send_keys("@Zahoder")
    button = browser.find_element(By.CSS_SELECTOR, 'div.second_block + [type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
