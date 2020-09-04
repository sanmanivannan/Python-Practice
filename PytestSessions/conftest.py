@pytest.fixture(params =['chrome','firefox'],scope='class')
def init__driver(request):
    if request.param == 'chrome':
        w_browser = webdriver.Chrome(ChromeDriverManager().install())

    if request.param == 'firefox':
        w_browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = w_browser

    yield
    w_browser.close()