import os

from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

from pages.common_actions_with_elements import CommonActionsWithElements


class ParentPage(CommonActionsWithElements):
    load_dotenv()
    base_url = os.environ.get('BASE_URL')

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        super().__init__(web_driver)
