import time

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class TestFileUpload:

    #@pytest.mark.smoke
    def tst_file_upload(self):

        """ 8/31/2021 Both Chrome and Gecko drivers were able to launch the Chrome and Fifefox browsers.  Woila """
        driver = webdriver.Chrome(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\chromedriver.exe')
        #driver = webdriver.Firefox(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\geckodriver.exe')
        #driver = webdriver.Ie(executable_path='C:\\Users\\qtvo9\\Dropbox\\Tools\\Selenium\\Driver\\IEDriverServer.exe')
        driver.implicitly_wait(3)
        driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

        driver.find_element_by_xpath("//input[@type='file']").send_keys('C:/Users/qtvo9/PycharmProjects/PythonSeleniumFramework/testData/TestImage.png')
        print('File path to upload selected successfully.')
        driver.find_element_by_xpath("//input[@value='Press']").click()

        time.sleep(3)

        txt = driver.find_element_by_xpath("//*[contains(text(), 'Your notes on the file were')]").text
        print(txt)
        assert 'You\'ve uploaded a file' in txt
        driver.close()