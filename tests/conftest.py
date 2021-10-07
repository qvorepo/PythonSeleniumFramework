import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from util.configurations import Configurations
from pathlib import Path

driver = None

@pytest.fixture(scope='class')
def setup(request):

    """ Get the drivers from the config ini file"""
    instance = Configurations()
    cfg = instance.config
    global driver

    browser_name = request.config.getoption("--browser_name")
    if browser_name == 'chrome':
        #driver = webdriver.Chrome(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\chromedriver.exe')
        driver = webdriver.Chrome(executable_path=cfg['default']['chrome_driver_path'])
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(
            executable_path=cfg['default']['firefox_driver_path'])
    elif browser_name == 'IE':
        driver = webdriver.Ie(executable_path=cfg['default']['IE_driver_path'])

    #driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.get(cfg['default']['url'])
    #driver.implicitly_wait(3)
    driver.implicitly_wait(cfg['default']['wait_time'])
    driver.maximize_window()
    request.cls.driver = driver

    yield# yield means to teardown.  It will be executed afterwards.
    driver.close()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    #driver.get_screenshot_as_file(name)
    driver.get_screenshot_as_file('../reports/' + name)