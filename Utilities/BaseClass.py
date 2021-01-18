
# Wrap tests in class so we don't need to pass 'setup' as argument to each test function
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Utilities.imports import MAX_WAIT
import pytest


@pytest.mark.usefixtures("setup_teardown")
class BaseClass:

    def exceptionFunc(self, exception):
        logger = self.get_logger()
        logger.info("Exception:", exception), print("EXCEPTION:", exception)
        return

    def verifyLinkPresence(self, linkText):
        try:
            WebDriverWait(self.driver, MAX_WAIT).until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))
        except TimeoutException as exception:
            self.exceptionFunc(exception)

    def verifyXpathPresence(self, xpath):
        try:
            WebDriverWait(self.driver, MAX_WAIT).until(EC.presence_of_element_located((By.LINK_TEXT, xpath)))
        except TimeoutException as exception:
            self.exceptionFunc(exception)

    def verifyIdPresence(self, ID):
        try:
            WebDriverWait(self.driver, MAX_WAIT).until(EC.presence_of_element_located((By.ID, ID)))
            self.driver.find_element(By.XPATH, "//*[@id='PopupNewUser']/div/button").click()
        except:
            return
