#There are 3 kinds of the waits
#STATIC WAIT
#1. Sleep
#static wait is also otherwise called as Sleep, which is the fixed wait time which will never change.
#there are alot of disadvantages using the static wait when comparing the dynamic wait

#DYNAMIC WAIT
#2. ImplicitWait
#Implicitwait can be used ONLY for the webelement/webelements
#global wait applicable for the whole program until and unless its changed
#Implicit wait will be applicable for all the webelements, unless its overrided
#Implicitwait cant be customized for each elements


#3. WebdriverWait(other wise called as Explicit wait)
# Explicitlywait is NOT limited to the webelements,can be used for elements like non-webelemets

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec #Should use expected_conditions method when using the WebDriverWait Method
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')
wait = WebDriverWait(driver,10)
wait.until(ec.title_is('HubSpot Login'))
print(driver.title)

emailid = wait.until(ec.presence_of_element_located((By.ID, 'username')))
emailid.send_keys('test@gmail.com')

driver.find_element(By.ID,'password').send_keys('password')

