import unittest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages import login_page, dashboard_page, new_user_signup_page, marketplace_page, node_deployment_page

import logging


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.testName = self._testMethodName
        self.web_driver = self.init_driver()
        self.web_driver.maximize_window()
        self.web_driver.implicitly_wait(5)

        self.login_page = login_page.LoginPage(self.web_driver)
        self.dashboard_page = dashboard_page.Dashboard(self.web_driver)
        self.new_user_signup_page = new_user_signup_page.NewUserSignUpPage(self.web_driver)
        self.marketplace_page = marketplace_page.Marketplace(self.web_driver)
        self.node_deployment_page = node_deployment_page.NodeDeployment(self.web_driver)

        load_dotenv()
        self.user_email=os.environ.get('USER_EMAIL')
        self.valid_user_email=os.environ.get('USER_EMAIL_VALID')
        self.user_password=os.environ.get('USER_PASSWORD')
        self.test_ssh_key=os.environ.get('SSH_KEY')
        self.promo_code=os.environ.get('PROMOCODE')

    def tearDown(self):
        self.web_driver.quit()
        self.logger.info('Browser was closed')
        self.logger.info(f'------ {self.testName} was ended------------')

    @staticmethod
    def init_driver():
        browser = 'chrome'  # You can change this to any browser you want to use
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
        return web_driver


if __name__ == '__main__':
    unittest.main()
