import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://crm.topnlab.ru")

time.sleep(3)

driver.find_elements("tag name", "a")[0].click()

time.sleep(2)