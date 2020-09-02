from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_login_amazon():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.amazon.com/')
    driver.implicitly_wait(5)
    print(driver.title)
    assert driver.title == "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"
    driver.quit()

def test_login_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/')
    driver.implicitly_wait(5)
    print(driver.title)
    assert driver.title == "Google"
    driver.quit()

def test_login_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(5)
    print(driver.title)
    assert driver.title == "Facebook"
    driver.quit()

"""
to execute the test cases, as usual, execute the below command
py.test PytestSessions\test_webpage_login.py

to execute the test cases PARALLELLY
py.test PytestSessions\test_webpage_login.py -n 3

"""
