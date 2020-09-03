from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params =['chrome','firefox'],scope='class')
def web_browser(request):
    if request.param == 'chrome':
        w_browser = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        w_browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = w_browser
    yield
    w_browser.close()

@pytest.mark.usefixtures('web_browser')
class Base_Class():
    pass
class Test_Title_Check(Base_Class):
    def test_title_check(self):
        self.driver.get("www.google.com")
        self.driver.implicitly_wait(10)
        assert self.driver.title == 'Google'
    def test_url_check(self):
        self.driver.implicitly_wait(10)
        assert self.driver.current_url == 'www.google.com'


