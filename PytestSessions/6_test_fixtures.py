from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("===========setup============")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.youtube.com/")

    yield
    print("==========teardown==========")
    driver.quit()

def test_login_amazon(init_driver):
    assert driver.title == "YouTube"

def test_url_check(init_driver):
    assert driver.current_url == 'https://www.youtube.com/'

"""#The above testcases can also be written using the MARKER

@pytest.mark.usefixtures("init_driver")    
def test_login_amazon():
    assert driver.title == "YouTube"

@pytest.mark.usefixtures("init_driver")   
def test_url_check():
    assert driver.current_url == "https://www.youtube.com/"
"""