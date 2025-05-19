import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://crm.topnlab.ru")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "login-block__btn").click()
time.sleep(3)