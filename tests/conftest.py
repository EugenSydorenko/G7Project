import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.login_page import LoginPage
from pages import login_page, dashboard_page, new_user_signup_page, marketplace_page, node_deployment_page


@pytest.fixture(scope="class")
def web_driver(request):
    browser = "chrome"  # You can change this to any browser you want to use
    if browser.lower() == 'chrome':
        ops = ChromeOptions()
        ops.add_argument('--remote-allow-origins=*')
        web_driver = webdriver.Chrome(options=ops)
    elif browser.lower() == 'firefox':
        ops = FirefoxOptions()
        web_driver = webdriver.Firefox(options=ops)
    elif browser.lower() == 'safari':
        ops = SafariOptions()
        web_driver = webdriver.Safari(options=ops)
    elif browser.lower() == 'edge':
        ops = EdgeOptions()
        web_driver = webdriver.Edge(options=ops)
    elif browser.lower() == 'remote':
        cap = DesiredCapabilities.CHROME.copy()
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        cap.update(chrome_options.to_capabilities())
        web_driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub'
        )
    else:
        raise ValueError('Invalid browser specified.')
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()


@pytest.fixture(autouse=False)
def setup_teardown(self, web_driver):
    self.logger = logging.getLogger(__name__)
    self.testName = self._testMethodName
    self.driver = web_driver
    self.driver.maximize_window()
    self.driver.implicitly_wait(5)

    yield web_driver

    self.driver.quit()
    self.logger.info("Browser was closed")
    self.logger.info(f"------ {self.testName} was ended------------")


# Fixtures for pages
@pytest.fixture(scope="class")
def login_page(web_driver):
    return LoginPage(web_driver)


@pytest.fixture(scope="class")
def dashboard_page(web_driver):
    return Dashboard_page(web_driver)


@pytest.fixture(scope="class")
def new_user_signup_page(web_driver):
    return New_user_signup_page(web_driver)


@pytest.fixture(scope="class")
def marketplace_page(web_driver):
    return Marketplace_page(web_driver)


@pytest.fixture(scope="class")
def node_deployment_page(web_driver):
    return Node_deployment_page(web_driver)


@pytest.fixture()
def web_driver_chrome(request):
    ops = ChromeOptions()
    ops.add_argument('--remote-allow-origins=*')
    return webdriver.Chrome(options=ops)
