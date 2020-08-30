from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

#First way of doing/bypassing the certificate issue
"""options = webdriver.ChromeOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://expired.badssl.com/")"""

#Second way of doing/byp[assing the certificate issue

desiredcapabilities = DesiredCapabilities()
desiredcapabilities.CHROME().copy()
desiredcapabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://expired.badssl.com/")