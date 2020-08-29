from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
#We use ChromeOptions method for HEADLESS OPERATIONS for Chrome browser
options = webdriver.ChromeOptions()
options.headless = True
#options.add_argument("--incognito") #can use add_argument to run on incognito mode as well


"""#We use ChromeOptions method for HEADLESS OPERATIONS for Firefox browser
options = webdriver.FirefoxOptions()
options.headless = True

#We use ChromeOptions method for HEADLESS OPERATIONS for IE browser
options = webdriver.IeOptions()
options.headless = True"""

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#In case if you are using without the webdriver manager also.,we can use the headless options
#driver = webdriver.Chrome(executable_path="D:\\Learning\\Driver files\\chromedriver.exe", options=options)

driver.get("https://www.amazon.in/")
print(driver.title)
