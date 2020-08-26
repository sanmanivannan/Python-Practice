'''
Select from the drop down
Deselect from the drop down #You may only deselect all options of a multi-select
Write functions to avoid repeated usage of Select from the drop down
Write functions to list all the OPTIONS available on the drop down menu
'''
from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

#num_emp = driver.find_element(By.NAME,'NoOfEmployees')
#select = Select(num_emp)
#select.select_by_value('Automotive')
#select.select_by_visible_text('Automotive')
#select.select_by_index(4)

#ele_indus = driver.find_element(By.NAME,'Industry')
#select = Select(ele_indus)
#select.select_by_value('Automotive')
#select.select_by_visible_text('Automotive')
#select.select_by_index(4)

#country = driver.find_element(By.NAME,'Country')
#select = Select(country)
#select.select_by_value('India')
#select.select_by_visible_text('Automotive')
#select.select_by_index(4)

#To find whether the dropdown is multi select or not
#print(select.is_multiple)

#You may only deselect all options of a multi-select
#select.deselect_all()
#select.deselect_by_index(4)
#select.deselect_by_value()
#select.deselect_by_visible_text()

#instead of writing the Select statesments again and again repeatedly for the dropdowns,
#we write the user defined functions as mentioned below, so that it could be reused when ever needed

#def select_fun(ele,value):
#    select1 = Select(ele)
#    select1.select_by_value(value)

#ele1 = driver.find_element(By.NAME, 'Country')
#ele1_indus = driver.find_element(By.NAME,'Industry')
#select_fun(ele1,'United States')
#select_fun(ele1_indus,'Travel')


#below is the user defined function to list out and print all the options on a dropdown menu
def select_list(ele):
    select2 = Select(ele)
    dropdownlist = select2.options
    print(len(dropdownlist))
    for i in dropdownlist:
        print(i.text)
        if (i.text) == "Travel":
            select2.select_by_visible_text("Travel")


ele2 = driver.find_element(By.NAME, 'Industry')
select_list(ele2)
