import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link1 = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    x_element = browser.find_element_by_*(selector)
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_tag_id('answer')
    input1.send_keys(y)
   
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла