from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.parent_page import ParentPage
from selenium.webdriver.support import expected_conditions as EC


class Dashboard(ParentPage):
    button_log_out = By.ID, 'Logout'
    button_add_node = By.ID, 'buttonAddNode'

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def __button_logout_element(self) -> WebElement:
        self.web_driver_wait_15.until(EC.element_to_be_clickable(self.web_driver.find_element(*self.button_log_out)))
        return self.web_driver.find_element(*self.button_log_out)

    def __button_add_node_element(self) -> WebElement:
        return self.web_driver.find_element(*self.button_add_node)

    def is_button_log_out_displayed(self) -> bool:
        button_log_out: WebElement = self.__button_logout_element()
        return self._is_element_displayed(button_log_out)

    def click_on_button_add_node(self):
        button_add_node: WebElement = self.__button_add_node_element()
        self._click_on_element(button_add_node)
