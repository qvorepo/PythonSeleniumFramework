from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from selenium.webdriver.support.select import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href *='shop']") #tuple

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    ice_cream_checkbox = (By.ID, "exampleCheck1")
    submit_btn = (By.XPATH, "//input[@type='submit']")
    success_msg = (By.CSS_SELECTOR, '.alert-success')
    gender = (By.ID, "exampleFormControlSelect1")
    employ_status = (By.XPATH, "//input[@value='option1']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # * will read the variable as a tuple
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_ice_cream_checkbox(self):
        return self.driver.find_element(*HomePage.ice_cream_checkbox)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_success_msg(self):
        return self.driver.find_element(*HomePage.success_msg)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def validate_form_submission(self):
        assert 'Success!' in self.get_success_msg().text

    def get_employment_status(self):
        return self.driver.find_element(*HomePage.employ_status)