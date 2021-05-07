from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link1 = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    treasure = browser.find_element_by_id("input_value")
    x = treasure.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла