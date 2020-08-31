from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec #Should use expected_conditions method when using the WebDriverWait Method
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
"""import xlrd
wb = xlrd.open_workbook("new.xlsx")
sht = wb.sheet_by_name("Sheet1")
row = sht.nrows
col = sht.ncols
#print(row)
#print(col)

for i in range(1, row):
    uname = sht.cell_value(i,0)
    pass1 = sht.cell_value(i,1)
    print(uname + " " + pass1)"""

import xlrd
wb = xlrd.open_workbook("new1.xlsx")
sht = wb.sheet_by_name("registration")
row = sht.nrows
col = sht.ncols
print(row)
print(col)


"""def seletopt(sellopt,value):
    select = Select(sellopt)
    sel_opt = select.options
        for j in sellopt:
        if (j.text) == value:            
            sellopt.send_keys(value)
            break"""


def seletopt(sellopt, value):
    for j in sellopt:
        if (j.text) == value:
            j.click()
            break

for i in range(1, row):
    url = sht.cell_value(i,0)
    fname = sht.cell_value(i,1)
    lname = sht.cell_value(i,2)
    email = sht.cell_value(i,3)
    jobtitle = sht.cell_value(i,4)
    company = sht.cell_value(i,5)
    phone1 = sht.cell_value(i,6)
    noofemp = sht.cell_value(i,7)
    industry = sht.cell_value(i,8)
    country = sht.cell_value(i,9)
    #print(url +  fname +  lname +  email +  jobtitle + company +  phone +  noofemp +  industry + country)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

    url1 = driver.find_element(By.ID,'Form_submitForm_subdomain')
    url1.clear()
    url1.send_keys(url)

    f_name = driver.find_element(By.ID,'Form_submitForm_FirstName')
    f_name.clear()
    f_name.send_keys(fname)

    l_name = driver.find_element(By.ID,'Form_submitForm_LastName')
    l_name.clear()
    l_name.send_keys(lname)

    e_mail = driver.find_element(By.ID,'Form_submitForm_Email')
    e_mail.clear()
    e_mail.send_keys(email)

    job_title = driver.find_element(By.ID,'Form_submitForm_JobTitle')
    job_title.clear()
    job_title.send_keys(jobtitle)

    company_name = driver.find_element(By.ID,'Form_submitForm_CompanyName')
    company_name.clear()
    company_name.send_keys(company)

    contact_num = driver.find_element(By.NAME,'Contact')
    contact_num.clear()
    contact_num.send_keys(phone1)

    no_of_emp = driver.find_elements(By.ID, 'Form_submitForm_NoOfEmployees')
    no_of_emp.clear()
    seletopt(no_of_emp,noofemp)

    indus = driver.find_element(By.ID, 'Form_submitForm_Industry')
    indus.clear()
    seletopt(indus, industry)

    cont = driver.find_element(By.ID, 'Form_submitForm_Country')
    cont.clear()
    seletopt(cont, country)


"""def seletopt(sellopt,value):
    for j in sellopt:
        if (j.text) == value:
            no_of_emp.clear()
            no_of_emp.send_keys(value)

    no_of_emp = driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
    no_of_emp.clear()
    no_of_emp.send_keys(noofemp)

    indus = driver.find_element(By.ID,'Form_submitForm_Industry')
    indus.clear()
    indus.send_keys(industry)

    cont = driver.find_element(By.ID,'Form_submitForm_Country')
    cont.clear()
    cont.send_keys(country)"""



