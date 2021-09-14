from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country_input = (By.XPATH, "//input[@id='country']")
    purchase_btn = (By.XPATH, "//input[@value='Purchase']")
    confirm_msg = (By.XPATH, "//div[contains(@class, 'alert-success')]")

    # 'Success! Thank you! Your order will be delivered in next few weeks :-).'
    successTxt = 'Success!'
    successTxt2 = 'Thank you! Your order will be delivered in next few weeks'

    def get_country_input(self):
        return self.driver.find_element(*ConfirmPage.country_input)

    def purchase_items(self):
        self.driver.find_element(*ConfirmPage.purchase_btn).click()

    def get_confirm_msg(self):
        return self.driver.find_element(*ConfirmPage.confirm_msg)

    def validate_checkout_success(self):
        assert ConfirmPage.successTxt in self.driver.find_element(*ConfirmPage.confirm_msg).text
        assert ConfirmPage.successTxt2 in self.driver.find_element(*ConfirmPage.confirm_msg).text
