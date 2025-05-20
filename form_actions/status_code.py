import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")

LINK_LIST = driver.find_elements('xpath', "//ul/li/a")

for link in LINK_LIST:
    link.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

print(LINK_LIST)