from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec #Should use expected_conditions method when using the WebDriverWait Method
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# This practice is for knowing the javascripts which could be implimented alone with python selenium

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.com/')

bestseller = driver.find_element(By.LINK_TEXT, 'Best Sellers')

"""#syntax for executing the JS within selenium
#click using the JS
driver.execute_script("arguments[0].click();", bestseller)

#display using JS
title = driver.execute_script("return document.title;")
print(title)

#refresh the page using the JS
driver.execute_script("history.go(0);")

#introducing alerts in the JS
driver.execute_script("alert('Hello!!!');")

#JS to print all text available on the page
innertext = driver.execute_script('return document.documentElement.innerText;')
print(innertext)"""

#JS yo put a border line around any element
driver.execute_script('argument[0].style.border = "3x solid red";', bestseller)

#driver.execute_script("document.getElementById('username').value = 'test1';")

#document.getElementById('username').value = 'test1';

#alert("hi")