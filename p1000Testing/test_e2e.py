# This file contains the tests

from selenium.webdriver.common.keys import Keys
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
from p1000Testing.Logger import Logger
from Utilities.imports import BASE_URL
import inspect
import pytest
import time
import sys
import re


class Tests(Logger, BaseClass):

    @staticmethod
    def find_cheapest_result(resultList, homePage, getParams):
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
            print("Choosing cheapest item that matches results")
            itemPage.goToCheckout(), print("Navigating to checkout page")
            time.sleep(1), print("Minimum price is:", temp_min)
        else:
            print("0 results")

    def test_first(self, getParams):
        logger = self.get_logger(); print("Logger created")
        homePage = HomePage(self.driver)
        homePage.searchItem().send_keys(getParams["item_name"], Keys.RETURN)
        print(f"Searching for: {getParams['item_name']}")
        resultList = homePage.getSearchResults()
        self.find_cheapest_result(resultList, homePage, getParams)
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3], "PASSED!")

    @pytest.mark.skip  # TODO
    def test_second(self):
        """"This test should fail"""
        logger = self.get_logger()
        logger.info(inspect.stack()[0][3] + " This test should fail"), print(inspect.stack()[0][3], "This test should fail")
        # assert 1 == 2

    @pytest.mark.skip(reason="Because don't need it at the moment")
    def test_third(self):
        """"This test should skip"""
        logger = self.get_logger()
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3], "PASSED!")

    @pytest.mark.skipif(sys.version_info > (3, 5), reason="Python version is greater than 3.5")
    def test_forth(self):
        """"This test should skip if Python version is greater than 3.5"""
        logger = self.get_logger()
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3],
                                                              "Will be skipped if Python version is lower than 3.5")

    @pytest.mark.windows  # Command to run only smoke keyword tests: py.test -m <keyword> (optional: -v -s)
    def test_UI_1(self):  # Command to run tests by regex: py.test -k <regex-here> (optional: -v -s)
        logger = self.get_logger()
        self.driver.get(BASE_URL), print("Navigate to home page")
        homePage = HomePage(self.driver)
        loginPage = homePage.navToLogin(); print("Navigate to login")
        loginPage.verifyCheckDigit(ID="123", password="abc"), print("Verifying check-digit")
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3], "PASSED!")

    @pytest.mark.windows
    @pytest.mark.nightly
    def test_UI_2(self):
        logger = self.get_logger()
        time.sleep(10)  # TODO
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3], "PASSED!")

    @pytest.mark.skip  # TODO
    @pytest.mark.iOS
    def test_UI_3(self):
        logger = self.get_logger()
        logger.info(inspect.stack()[0][3] + " PASSED"), print(inspect.stack()[0][3], "PASSED!")

# MULTI-BROWSER TESTING #
# def test_cross_browser(cross_browser):
#     print(cross_browser)
