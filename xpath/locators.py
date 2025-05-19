from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")

LOGO = ('xpath', '(//nav//a[@href='/'])')

CATALOG_DROPDOWN_BUTTON = ('xpath', "(//div[contains(@class, 'navbar-nav-collapse')])//a[text()=' Catalog ']")

SIGN_IN_BUTTON = ('xpath', "//button//span[text()=' Sign in ']")
START_FOR_FREE_BUTTON = ('xpath', "//button//span[text()=' Start for free ']")
PRICING_BUTTON = ('xpath', "//li//a[text()=' Pricing ']")
FOR_BUSINESS_BUTTON = ('xpath', "//li//a[text()=' For Business ']")
ALL_COURSES_BUTTON = ('xpath', "//div[contains(@class, 'categories')]/a[text()='All courses ']")