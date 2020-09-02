# https://pypi.org/project/webdriver-manager/ path of the webdriver manager for managing the webbrowsers

from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

browser_name= "chrome"

if browser_name == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser_name == "safari":
    driver = webdriver.Safari()
else:
    print("please enter the correct browser name" + browser_name )
    raise Exception("Driver is not found")

driver.implicitly_wait(5)

driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, "username").send_keys("usename1@gmail.com")
driver.find_element(By.ID, "password").send_keys("password1")
driver.find_element(By.ID, "loginBtn").click()
print(driver.title)

time.sleep(5)
driver.quit()


