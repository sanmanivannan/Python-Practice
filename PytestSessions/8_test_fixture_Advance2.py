import pytest

"""
#Instead of having the FIXTURES(aka.,setup and teardown) with in the actual testcases;
#we can write the FIXTURES separatly in the ""conftest.py"" file and can be used for any testcases within that forlder

@pytest.fixture(params =['chrome','firefox'],scope='class')
def init__driver(request):
    if request.param == 'chrome':
        w_browser = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        w_browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = w_browser

    yield
    w_browser.close()"""

@pytest.mark.usefixtures('init__driver')
class BaseTest:
    pass

class Test_Check(BaseTest):

    def test_get_website(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(10)

    def test_title_check(self):
        assert self.driver.title == 'Google'

    def test_url_check(self):
        self.driver.implicitly_wait(10)
        assert self.driver.current_url == 'https://www.google.com/'
        self.driver.implicitly_wait(10)
