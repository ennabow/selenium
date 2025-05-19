import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://intelion.cloud")
current_url = driver.current_url
current_title = driver.title

assert current_url == "https://intelion.cloud"

print(current_url, current_title)

