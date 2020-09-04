import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('init__driver')
class BaseTest:
    pass

class Test_Checker(BaseTest):
    @pytest.mark.parametrize("username , password",
                                [
                                    ("uname1", "pword1"),
                                    ("uname2", "pword2")
                                ]
                            )
    def test_get_website(self, username, password):
        self.driver.get("https://app.hubspot.com/login/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
