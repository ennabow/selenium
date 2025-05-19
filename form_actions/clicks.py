import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://crm.topnlab.ru')

FERGOT_PASSWORD_BUTTON = driver.find_element('xpath', "//div/a[text()=' Забыли пароль? ']")
FERGOT_PASSWORD_BUTTON.click()

EMAIL_FIELD = driver.find_element('xpath', "//input[@placeholder='Введите адрес электронной почты']")

EMAIL_FIELD.send_keys("a@to.ru")

time.sleep(3)