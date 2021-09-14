import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from util.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, get_data):
        log = self.get_logger()
        homePage = HomePage(self.driver)

        homePage.get_name().send_keys(get_data["firstname"])
        log.info(("firstname: ") + get_data["firstname"])

        homePage.get_email().send_keys(get_data["email"])
        log.info(("email: ") + get_data["email"])

        homePage.get_ice_cream_checkbox().click()
        self.selectOptionsByText(homePage.get_gender(),get_data["gender"])
        log.info(("gender: ") + get_data["gender"])

        homePage.get_employment_status().click()

        homePage.get_submit_btn().click()

        #driver.get('https://rahulshettyacademy.com/angularpractice/')
        #driver.find_element_by_name("name").send_keys('Jane')
        #driver.find_element_by_id("exampleCheck1").click()
        #driver.find_element_by_xpath("//input[@type='submit']").click()
        #msg = driver.find_element_by_css_selector('.alert-success').text
       # print(msg)

        homePage.validate_form_submission()
        self.driver.refresh()
        #driver.close()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def get_data(self, request):
        return request.param