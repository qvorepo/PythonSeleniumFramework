import time

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestFileDownload:

    @pytest.mark.smoke
    def test_file_download(self):

        #fp = webdriver.FirefoxProfile()
        #fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf")
        #fp.set_preference("browser.download.manager.showWhenStart", False)

        """ 8/31/2021 Both Chrome and Gecko drivers were able to launch the Chrome and Fifefox browsers.  Woila """
        #driver = webdriver.Chrome(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\chromedriver.exe')
        driver = webdriver.Firefox(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\geckodriver.exe',)
        #driver = webdriver.Ie(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\IEDriverServer.exe')
        driver.implicitly_wait(3)
        driver.get('https://notepad-plus-plus.org/downloads/')

        driver.find_element_by_partial_link_text('8.1.4').click()
        driver.find_element_by_xpath("//a[contains(@href,'npp.8.1.4.Installer.x64.exe')]").click()

        #npp.8.1.4.Installer.x64.exe
        driver.close()