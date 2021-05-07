import math
from selenium import webdriver
import time 

link1 = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    print (x)
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    print (y)
    elem = str(int(x)+int(y))
    print (elem)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(elem) # ищем элемент с текстом 

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла