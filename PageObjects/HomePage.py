
# Home page

from selenium.webdriver.common.action_chains import ActionChains
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from PageObjects.ItemPage import ItemPage
from Utilities.BaseClass import BaseClass
import time


class HomePage(BaseClass):

    registerButton = (By.XPATH, "//*[@id='form1']/div[1]/div/div[2]/ul/li[1]/div/div/div/ul/li[1]")
    searchResults = (By.XPATH, "//*[@id='scrollingcontent']/div/ul/child::li")
    myAccount = (By.LINK_TEXT, "P1000 שלי")
    searchBar = (By.ID, "txtSearchBox")

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def getProdPath(index):
        return "//*[@id='scrollingcontent']/div/ul/li[" + str(index) + "]"

    def searchItem(self):
        return self.driver.find_element(*HomePage.searchBar)

    def getSearchResults(self):
        return self.driver.find_elements(*HomePage.searchResults)

    def getProdName(self, index):
        return self.driver.find_element(By.XPATH, self.getProdPath(index)).text.split("\n")[0]

    def getProdTitle(self, index):
        return self.driver.find_element(By.XPATH, self.getProdPath(index) + "/a/div[1]/div[3]/div/div/div").text

    def clickItem(self, itemIndex):
        self.driver.find_element(By.XPATH, "//*[@id='scrollingcontent']/div/ul/li[" + str(itemIndex) + "]").click()
        return ItemPage(self.driver)

    def navToLogin(self):
        self.verifyIdPresence("PopupNewUser")  # Close pop-up add if pops
        time.sleep(2)
        self.verifyLinkPresence(HomePage.myAccount[1])
        element_to_hover_on = self.driver.find_element(*HomePage.myAccount)
        registerElement = self.driver.find_element(*HomePage.registerButton)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_on).move_to_element(registerElement)
        # hover.perform()
        hover.click().perform()
        return LoginPage(self.driver)
