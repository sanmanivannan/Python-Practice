from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="D:\\Learning\\Driver files\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com")

driver.find_elements(By.NAME, "q").send_keys("Selenium Python")
#driver.find_element_by_name("q").send_keys("selenium python")
print(driver.title)

time.sleep(5)
driver.quit()



