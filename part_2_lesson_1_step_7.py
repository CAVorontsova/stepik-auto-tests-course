import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link1 = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    treasure = browser.find_element_by_id("treasure")
    x_element = treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
   
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла