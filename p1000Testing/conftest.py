
# This file is special Pytest (don't change the name of file)
# Here we put the fixtures (setup/teardown/data) so it will be global to program
from Utilities.imports import MAX_WAIT, URL, data
from selenium import webdriver
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")  # FLAG = run setup_teardown per class (and not on each function)
def setup_teardown(request):
    global driver
    print("$ SETUP $")
    browser_name = request.config.getoption("browser_name")  # Gets value from cmd (browser's name)
    if browser_name == "chrome":
        driver = webdriver.Chrome("C:/Users/Sahar.itzhak/Downloads/Chromedriver/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox("C:/Users/Sahar.itzhak/Downloads/drivers/geckodriver")
    elif browser_name == "IE":
        print("@#$%^&*((*&^%$#@!@#$%^&*()(*&^%$#@!#$%^&*(*&^%$#@")
        exit()
    else:
        print("Browser not supported")
        return
    driver.implicitly_wait(MAX_WAIT)
    driver.get(URL)
    request.cls.driver = driver  # Binds the driver to the class (Tests class)
    yield
    driver.quit()
    print("$ TEARDOWN $")


@pytest.fixture(params=["Chrome", "Firefox", "Internet Explorer"])
def cross_browser(request):
    return request.param


# CAPTURE SCREENSHOTS TO HTML REPORT ON FAILURE #
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails. :param item:"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# Parameters to send to test_e2e (instead of hard-code values)
@pytest.fixture(params=data)
def getParams(request):
    return request.param
