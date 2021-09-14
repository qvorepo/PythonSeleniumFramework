import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:
    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        #logger = logging.getLogger(__name__)
        logger = logging.getLogger(loggerName)


        fileHandler = logging.FileHandler("logFile.log")
        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # filehandler object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, txt):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, txt)))

    def select_location(self, country):
        return self.driver.find_element(By.LINK_TEXT, country)

    def selectOptionsByText(self, locator, txt):
        options = Select(locator)
        options.select_by_visible_text(txt)


