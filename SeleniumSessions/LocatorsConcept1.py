"""
How to create web element using different locators:
ID
Name
Class Name
XPath
CSS Selector
Link Text
Partial Link Text
Tag Name

"""
from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

#FindElement By ID
driver.find_element(By.ID, "Form_submitForm_FirstName").send_keys("FName")

#FindElement By NAME
driver.find_element(By.NAME, "LastName").send_keys("LName")

#FindElement By CSS SELECTOR, just use the ID or Name value and have #in front of the value
driver.find_element(By.CSS_SELECTOR, "#Form_submitForm_JobTitle").send_keys("Manager")
# If you wish to use the CSS Selector using the class name from the inspect, just use like this( input.class1.class2.class3)
#driver.find_element(By.CSS_SELECTOR, "input.class1.class2.class3").send_keys("Manager")

#FindElement By CLASS_NAME. Always use only the unique class name if you have multiple class name in that parameter
#driver.find_element(By.CLASS_NAME, "email text").send_keys("test123@gmail.com")

#FindElement By XPATH
# If you wish to use the XPATH using the class name from the inspect, just use like this(//input[@class='class1 class2']
#driver.find_element(By.XPATH, "//input[@class='class1 class2']").send_keys("fnamelname")


#FindElement By LINK_TEXT(only for links)
#driver.find_element(By.LINK_TEXT, "Features").click()

#FindElement By PARTIAL_LINK_TEXT(only for links)
#driver.find_element(By.PARTIAL_LINK_TEXT, "Services").click()

#FindElement By TAG_NAME
links1 = driver.find_elements(By.TAG_NAME, "a")
print(len(links1))
#prints the list of hyperlinks on the links
for i in links1:
    print(i.text)
    print(i.get_attribute('href'))

#FindElement By TAG_NAME
imagelinks2 = driver.find_elements(By.TAG_NAME, "img")
print(len(imagelinks2))
#prints the list of images on the links
for j in imagelinks2:
    print(j.text)
    print(j.get_attribute('src'))




