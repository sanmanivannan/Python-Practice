from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Learning\\Driver files\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com")
print(driver.title)
#driver.implicitly_wait(5)
driver.find_element(By.NAME, "q").send_keys("Selenium Python")
#driver.find_element_by_class_name("pR49Ae gsfi").send_keys("selenium python")

optionslist = driver.find_elements(By.CSS_SELECTOR,"ul.erkvQe li span")
print(len(optionslist))

for i in optionslist:
    if i.text == "Selenium Python Tutorial":
        i.click()
        break

    print(i.text)



time.sleep(5)
driver.quit()



