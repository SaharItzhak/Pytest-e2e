
# Item page
from selenium.common.exceptions import NoSuchElementException
from PageObjects.CheckoutPage import CheckoutPage
from Utilities.BaseClass import BaseClass
from p1000Testing.Logger import Logger
from selenium.webdriver.common.by import By


class ItemPage(BaseClass, Logger):

    buyNowBtn = (By.ID, "MainContent_SaleDetailsData_Auctions_BuyNowBtn")

    def __init__(self, driver):
        self.driver = driver

    def goToCheckout(self, linkText):
        try:
            self.verifyLinkPresence(linkText)
        except NoSuchElementException:
            logger = self.get_logger()
            logger.info("$ Item is out of stock $")
            print("Out of stock")
            return
        self.driver.find_element(*ItemPage.buyNowBtn).click()
        return CheckoutPage(self.driver)
