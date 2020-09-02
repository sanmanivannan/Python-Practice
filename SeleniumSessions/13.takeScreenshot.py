from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
print(driver.title)
driver.get_screenshot_as_file('1.png')

#If we want to take the FULL ScreenSHOT of the page, we have to do it ONLY on the HEADLESS mode and use a LAMDBA function


