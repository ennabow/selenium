import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')

# сохраняем локаторы
FULL_NAME = driver.find_element('xpath', "//input[@id='userName']")
USER_EMAIL = driver.find_element('xpath', '//input[@id="userEmail"]')
CURRENT_ADDRESS = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
PERMANENT_ADDRESS = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')

# очищаем поля
FULL_NAME.clear()
USER_EMAIL.clear()
CURRENT_ADDRESS.clear()
PERMANENT_ADDRESS.clear()

# заполняем поля
FULL_NAME.send_keys("ola")
USER_EMAIL.send_keys("ola@alo.ru")
CURRENT_ADDRESS.send_keys("spb")
PERMANENT_ADDRESS.send_keys("moscow")

time.sleep(2)
# проверяем введенные значения
assert FULL_NAME.get_attribute('value') == "ola"
assert USER_EMAIL.get_attribute('value') == "ola@alo.ru"
assert CURRENT_ADDRESS.get_attribute('value') == "spb"
assert PERMANENT_ADDRESS.get_attribute('value') == "moscow"

time.sleep(2)

# очищаем поля
FULL_NAME.clear()
USER_EMAIL.clear()
CURRENT_ADDRESS.clear()
PERMANENT_ADDRESS.clear()