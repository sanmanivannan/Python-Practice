from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

#MOVE TO ELEMENT using ActoinChain Method
"""driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com/")
print(driver.title)
driver.maximize_window()

st_click = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
act_class = ActionChains(driver)
act_class.move_to_element(st_click).perform()

sec_click = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[1]/div[2]/div[2]/div/ul/li[16]/ul/li[2]/a')
act_class.move_to_element(sec_click).perform()
#sec_click.click()

thi_click = driver.find_element(By.XPATH, '/html/body/form/div[4]/div[1]/div[1]/div[2]/div[2]/div/ul/li[16]/ul/li[2]/ul/li[1]/a')
thi_click.click()

time.sleep(3)
driver.quit()"""

#DRAG AND DROP using ActoinChain Method

"""driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/droppable/")
print(driver.title)
#driver.maximize_window()

source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
act_chain = ActionChains(driver)
#act_chain.click_and_hold(source).act_chain.move_to_element(target).release().perform()

#act_chain.drag_and_drop(source, target).perform()"""

#RIGHT CLICK using ActoinChain Method
"""driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
print(driver.title)
#driver.maximize_window()
r_click = driver.find_element(By.XPATH, "//span[text()='right click me']")
act_chain = ActionChains(driver)
act_chain.context_click(r_click).perform()

opt_list = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-list span')
for i in opt_list:
    print(i.text)
    if i.text == 'Copy':
        i.click()
        break"""

