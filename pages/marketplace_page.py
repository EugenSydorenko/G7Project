from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.parent_page import ParentPage


class Marketplace(ParentPage):
    deploy_solana_node = By.XPATH, '//a[@href="/server-deployment/5"]'

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def __deploy_solana_node_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.deploy_solana_node)
        return element

    def click_on_solana_node_deploy_now(self):
        solana_node_deploy_now: WebElement = self.__deploy_solana_node_element()
        self._click_on_element(solana_node_deploy_now)
