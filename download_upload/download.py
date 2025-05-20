import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get("https://code.mu/ru/markup/book/supreme/")
#
# time.sleep(2)
#
# driver.find_elements('xpath', '//div[@data-w="nict/down"]//a')[0].click()
#
# time.sleep(2)

driver.get("https://the-internet.herokuapp.com/download")

files = driver.find_elements('xpath', "//div[@class='example']/a")

for file in files:
    file.click()

time.sleep(5)