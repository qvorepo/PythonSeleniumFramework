from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    #cards = (By.CSS_SELECTOR, ".card") #self.driver.find_elements_by_css_selector(".card")
    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, '.card-footer button')
    shopping_cart = (By.CSS_SELECTOR, '#navbarResponsive a.nav-link.btn-primary')
    cart_details = (By.XPATH, "//h4[@class='media-heading']/a")
    checkout = (By.XPATH, "//*[contains(text(), 'Checkout')]")


    #def get_cards(self):
    #    return self.driver.find_elements(*CheckoutPage.cards)

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckoutPage.card_footer)

    def get_shopping_cart(self):
        return self.driver.find_element(*CheckoutPage.shopping_cart)

    def get_cart_details(self):
        return self.driver.find_element(*CheckoutPage.cart_details)

    def checkout_items(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage




