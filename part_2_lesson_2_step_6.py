import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link1 = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    treasure = browser.find_element_by_id("input_value")
    x = treasure.text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

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