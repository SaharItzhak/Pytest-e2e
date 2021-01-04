
# This file contains the tests
from selenium.webdriver.common.keys import Keys
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from p1000Testing.Logger import Logger
import time
import sys
import re


class Tests(Logger, BaseClass):
    def test_first(self, getParams):
        logger = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.searchItem().send_keys(getParams["item_name"], Keys.RETURN)
        resultList = homePage.getSearchResults()
        if len(resultList):
            cheapestItemIndex = 0
            temp_min = sys.maxsize
            for i in range(1, len(resultList)):
                prodName = homePage.getProdName(i)
                if getParams["search_key"] in prodName.upper():
                    title = homePage.getProdTitle(i)
                    price = re.search(r"[0-9]+[,]?[0-9]*", str(title)).group()
                    intPrice = int(re.sub(",", "", price))
                    print(intPrice)
                    if temp_min > intPrice:
                        temp_min = intPrice
                        cheapestItemIndex = i

            itemPage = homePage.clickItem(cheapestItemIndex)  # Nav to item page
            itemPage.goToCheckout("קניה מהירה")
            time.sleep(2)
            print("Minimum price is:", temp_min)
            logger.info("**********TEST SECOND**********")
            print("**********TEST FIRST**********")
        else:
            logger.info("**********TEST SECOND**********")
            print("0 results")

    # @pytest.mark.skip
    # def test_second(self):
    #     logger = self.get_logger()
    #     logger.info("TEST SECOND***********************************")
    #     print("TEST SECOND**********************************")


# def test_cross_browser(cross_browser):
#     print(cross_browser)
