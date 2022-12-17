from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://vk.com/login"
browser = webdriver.Chrome()

try:

    browser.get(link)
    input1 = browser.find_element(By.ID, "index_email")
    input1.send_keys("89643446332")
    button = browser.find_element(By.CLASS_NAME, 'FlatButton')
    button.click()
    time.sleep(4)
    input2 = browser.find_element(By.NAME, 'password')
    input2.send_keys('Dzaga23122010')
    button2 = browser.find_element(By.CLASS_NAME, 'vkuiButton')
    button2.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
