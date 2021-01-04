
# Wrap tests in class so we don't need to pass 'setup' as argument to each test function
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Utilities.imports import MAX_WAIT
import pytest


@pytest.mark.usefixtures("setup_teardown")
class BaseClass:
    def verifyLinkPresence(self, linkText):
        WebDriverWait(self.driver, MAX_WAIT).until(EC.presence_of_element_located((By.LINK_TEXT, linkText)))

