from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver  #still not understanding what this line doesnt
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver #still not understanding what this line doesnt
    yield
    ff_driver.close()

@pytest.mark.usefixtures('init_chrome_driver')

class BaseClass:
    pass

class Test_Google_Chrome(BaseClass):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == 'Google'

    def test_google_url(self):
        assert self.driver.current_url == 'https://www.google.com/?gws_rd=ssl'


@pytest.mark.usefixtures('init_ff_driver')

class BaseClass:
    pass

class Test_Google_FF(BaseClass):

    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == 'Google'

    def test_google_url(self):
        assert self.driver.current_url == 'https://www.google.com/?gws_rd=ssl'



