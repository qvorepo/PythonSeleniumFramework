import time
from datetime import datetime
import pytest
# Implicit wait
# Explicit wait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from util.BaseClass import BaseClass

#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):
    def test_e2e(self):

        log = self.get_logger()
        homePage = HomePage(self.driver)

        """ Implicitly wait is global wait."""
        self.driver.implicitly_wait(3)
        wait = WebDriverWait(self.driver, 7)

        checkoutPage = homePage.shopItems()
        cards = checkoutPage.get_card_titles()
        log.info("Getting all the card titles.")

        i = -1
        for card in cards:
            i = i+1
            card_text = card.text

            log.info(card.text)
            if card.text == 'Blackberry':
                checkoutPage.get_card_footer()[i].click()
                # Shopping cart
                checkoutPage.get_shopping_cart().click()

                assert checkoutPage.get_cart_details().text == 'Blackberry'
                confirmPage = checkoutPage.checkout_items()

                confirmPage.get_country_input().send_keys("Ind")
                log.info("Entering country name as 'Ind'")
                #wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[contains(text(),'India')]")))
                self.verifyLinkPresence('India')

                self.select_location("India").click() #confirmPage.select_location_india()
                confirmPage.purchase_items()
                confirmPage.validate_checkout_success()
                log.info(("Received confirm message " + confirmPage.get_confirm_msg().text))

                assert 1 == 2

                print("Datetime: " + datetime.now().strftime('%m/%d/%Y'))

                self.driver.get_screenshot_as_file(
                    "{}{}{}".format("screen-shots/", datetime.now().strftime('%Y%m%d%H%M'), "-checkout-success.png"))

        #driver.close()
