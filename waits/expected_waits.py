import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://omayo.blogspot.com/')
wait = WebDriverWait(driver, 30, poll_frequency=1)
try:
   DISAPPEAR_TEXT = ("xpath", "//div[@id='deletesuccess']")
   wait.until(EC.invisibility_of_element_located(DISAPPEAR_TEXT))
   print('DISAPEAR_TEXT ok')

   APPEAR_TEXT = ("xpath", "//div[@id='delayedText']")
   wait.until(EC.invisibility_of_element_located(APPEAR_TEXT))
   print('APPEAR_TEXT ok')

   TIMER_BUTTON = ("xpath", "//input[@id='timerButton']")
   wait.until(EC.element_to_be_clickable(TIMER_BUTTON))
   print('TIMER_BUTTON ok')

   TRY_IT_BUTTON = ("xpath", "//button[text()='Try it']")
   wait.until(EC.element_to_be_clickable(TRY_IT_BUTTON)).click()
   MY_BUTTON = ("xpath", "//button[text()='Try it']")
   wait.until(EC.element_to_be_clickable(MY_BUTTON))
   print('MY_BUTTON ok')

finally:
    driver.quit()



