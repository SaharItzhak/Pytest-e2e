
# Home page
from selenium.webdriver.common.by import By
from PageObjects.ItemPage import ItemPage


class HomePage:

    searchResults = (By.XPATH, "//*[@id='scrollingcontent']/div/ul/child::li")
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

