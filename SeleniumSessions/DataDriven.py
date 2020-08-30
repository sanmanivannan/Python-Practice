from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec #Should use expected_conditions method when using the WebDriverWait Method
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import xlrd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('')

wb = xlrd.open_workbook("new.xlsx")
sht = wb.sheet_by_name("Sheet1")
row = sht.nrows
col = sht.ncols
print(row)
print(col)

for i in range(1, row):
    uname = sht.cell_value(i,0)
    pass1 = sht.cell_value(i,1)
    print(uname + " " +pass1)