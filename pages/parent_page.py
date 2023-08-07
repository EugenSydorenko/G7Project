from selenium.webdriver.remote.webdriver import WebDriver

from pages.common_actions_with_elements import CommonActionsWithElements


class ParentPage(CommonActionsWithElements):
    base_url = "https://platform.dev.edgevana.com"

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        super().__init__(web_driver)
