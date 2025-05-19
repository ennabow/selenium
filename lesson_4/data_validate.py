import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://intelion.cloud/")
url = driver.current_url
current_title = driver.title

print(url, current_title)

assert url == "https://intelion.cloud/", "err"



