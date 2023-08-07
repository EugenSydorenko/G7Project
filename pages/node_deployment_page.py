from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.parent_page import ParentPage


class NodeDeployment(ParentPage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.button_deploy_now = By.ID, 'buttonDeployNow'
        self.button_proceed = By.ID, 'buttonProceed'
        self.node_name_field = By.ID, 'formHorizontalNodeName'
        self.ssh_key_field = By.ID, 'formHorizontalEmail'
        self.promo_code_field = By.ID, 'formHorizontalPassword'
        self.terms_conditions_checkbox = By.ID, 'formHorizontalCheck'

    def __button_deploy_now_element(self) -> WebElement:
        button_deploy_now_element: WebElement = self.web_driver.find_element(*self.button_deploy_now)
        return button_deploy_now_element

    def __button_proceed_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.button_proceed)
        return element

    def __node_name_field_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.node_name_field)
        return element

    def __ssh_key_field_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.ssh_key_field)
        return element

    def __promo_code_field_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.promo_code_field)
        return element

    def __terms_of_service_and_conditions_checkbox_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.terms_conditions_checkbox)
        return element

    def click_on_button_deploy_now(self):
        button_deploy_now: WebElement = self.__button_deploy_now_element()
        self._click_on_element(button_deploy_now)

    def click_on_button_proceed(self):
        button_proceed: WebElement = self.__button_proceed_element()
        self._click_on_element(button_proceed)

    def click_terms_and_conditions_checkbox(self):
        terms_and_condition_checkbox: WebElement = self.__terms_of_service_and_conditions_checkbox_element()
        self._click_on_element(terms_and_condition_checkbox)

    def enter_node_name_into_node_name_field(self, node_name):
        node_name_field: WebElement = self.__node_name_field_element()
        self._enter_text_into_element(node_name_field, node_name)

    def enter_ssh_key_into_ssh_key_field(self, ssh_key):
        ssh_key_field: WebElement = self.__ssh_key_field_element()
        self._enter_text_into_element(ssh_key_field, ssh_key)

    def enter_promo_code_into_promo_code_field(self, promo_code):
        promo_code_field: WebElement = self.__promo_code_field_element()
        self._enter_text_into_element(promo_code_field, promo_code)
