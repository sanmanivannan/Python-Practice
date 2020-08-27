from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
print(driver.title)

driver.find_element(By.ID, 'justAnInputBox').click()
time.sleep(5)
#dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

#simple logic for selecting the single option from the jquery dropdown
"""for i in dropdown_list:
    print(i.text)
    if i.text == "choice 2 1":
        i.click()
        break"""

#Write a function for the above logic to click an option from the jquery dropdown
"""def select_options(droplist,value):
    for j in droplist:
        if j.text == value:
            j.click()
            break
#provide the list and values as mentioned below
#however, we cant always provide option selection values one by one if we have multiple selection, as its a crudew method
select_options(dropdown_list,'choice 6')
select_options(dropdown_list,'choice 2')
select_options(dropdown_list,'choice 5')"""

#Instead of providing the value one by one, have the values in the form of LIST
"""def select_options(droplist,value):
    for i in droplist:
        print(i.text)
        for j in range(len(value)):
         if i.text == value[j]:
            i.click()
            break

dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
#value1 = ['choice 2 1'] #single select 
value1 = ['choice 1', 'choice 6', 'choice 2 1'] #multi select
select_options(dropdown_list, value1)"""

#including the select ALL option too

def select_options(droplist,value):
    if value[0] != 'all':
      for i in droplist:
        print(i.text)
        for j in range(len(value)):
         if i.text == value[j]:
            i.click()
            break
    else:
        try:
         for k in droplist:
          k.click()
        except Exception as e:
            print(e)

dropdown_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value1 = ['all'] #select all
select_options(dropdown_list, value1)


