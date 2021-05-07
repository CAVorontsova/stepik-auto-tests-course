from selenium import webdriver
import time


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла