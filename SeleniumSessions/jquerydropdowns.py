from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
print(driver.title)