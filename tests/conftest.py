import pytest
import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--baseurl",
        action="store",
        default="baseurl",
        help="base URL for the AUT"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="the name of the browser you want to test with"
    )


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()

    if config.browser == "chrome":
        binary = 'D:/daily_smoke/vendors/chromedriver'
        chrome_options = Options()
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument("--incognito")
        driver_ = webdriver.Chrome(binary, chrome_options=chrome_options)
        driver_.maximize_window()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_
