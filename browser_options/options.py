import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--ignore-certificate-errors")

# chrome_options.add_argument("--window-size=500,500")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(1200,700)
driver.get("https://google.com")
time.sleep(2)