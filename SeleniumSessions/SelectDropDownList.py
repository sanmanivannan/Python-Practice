'''
Select from the drop down
Deselect from the drop down
is
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


ele_indus = driver.find_element(By.NAME,'Industry')
select = Select(ele_indus)
#select.select_by_value('Automotive')
#select.select_by_visible_text('Automotive')
select.select_by_index(4)


#You may only deselect all options of a multi-select
#select.deselect_all()
#select.deselect_by_index(4)
#select.deselect_by_value()
#select.deselect_by_visible_text()






