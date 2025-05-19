from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)