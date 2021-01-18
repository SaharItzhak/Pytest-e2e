
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    passwordInput = (By.ID, "loginPsw")
    idInput = (By.ID, "loginTz")

    def __init__(self, driver):
        self.driver = driver

    def verifyCheckDigit(self, ID, password):
        """Verify that ID is correct by calculating check digit"""
        self.verifyIdPresence("לקוח קיים? התחבר")
        self.driver.find_element(*LoginPage.idInput).send_keys(ID)
        self.driver.find_element(*LoginPage.passwordInput).send_keys(password, Keys.RETURN)
        self.verifyIdPresence("נא להזין מספר ת.ז. כולל סיפרת ביקורת")
