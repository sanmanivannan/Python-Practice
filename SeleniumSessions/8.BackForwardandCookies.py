from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
print(driver.title)
driver.implicitly_wait(5)
driver.find_element(By.ID, "nav-link-prime").click()
#Using BACK and FORWARD
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()

#Getting the COOKIES
cook = driver.get_cookies()
print(cook)

