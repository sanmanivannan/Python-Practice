from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.youtube.com/")

def teardown_module(module):
    driver.quit()

def test_login_amazon():
    assert driver.title == "YouTube"

def test_url_check():
    assert driver.current_url == "https://www.youtube.com/"
