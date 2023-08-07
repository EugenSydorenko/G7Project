import logging

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonActionsWithElements:
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.web_driver_wait_10 = WebDriverWait(self.web_driver, 10)
        self.web_driver_wait_15 = WebDriverWait(self.web_driver, 15)
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def __print_error_and_stop_test(e):
        logging.error('Can not work with element', e)
        assert False, 'Can not work with element ' + str(e)

    @staticmethod
    def __get_element_name(web_element: WebElement) -> str:
        try:
            name_attribute = web_element.get_attribute('name')
            return name_attribute if name_attribute else web_element.get_attribute('id')
        except Exception:
            return ''

    # def find_element_safely(self, locator) -> WebElement:
    #     locator_type = locator[0]
    #     locator_value = locator[1]
    #     try:
    #         return self.web_driver.find_element(*locator)
    #     except NoSuchElementException:
    #         raise AssertionError(f"Element with locator {locator_type}='{locator_value}' not found on the page.")

    def _is_element_displayed(self, web_element: WebElement) -> bool:
        try:
            self.web_driver_wait_10.until(EC.element_to_be_clickable(web_element))
            state = web_element.is_displayed()
            if state:
                message = self.__get_element_name(web_element) + ' Element is displayed'
            else:
                message = self.__get_element_name(web_element) + ' Element is not displayed'
            self.logger.info(message)
            return state
        except Exception:
            self.logger.error('Element is not displayed')
            return False

    def _click_on_element(self, xpath: str):
        try:
            web_element = self.web_driver.find_element(By.XPATH, xpath)
            self._click_on_element(web_element)
        except Exception as e:
            self.__print_error_and_stop_test(e)

    def _click_on_element(self, web_element: WebElement):
        try:
            self.web_driver_wait_10.until(EC.element_to_be_clickable(web_element))
            name = self.__get_element_name(web_element)
            web_element.click()
            self.logger.info(name + ' Element was clicked')
        except Exception as e:
            self.__print_error_and_stop_test(e)

    def _enter_text_into_element(self, web_element: WebElement, text: str):
        try:
            self.web_driver_wait_15.until(EC.visibility_of(web_element))
            web_element.clear()
            web_element.send_keys(text)
            self.logger.info(text + ' was inputted into element ' + self.__get_element_name(web_element))
        except Exception as e:
            self.__print_error_and_stop_test(e)

    def user_opens_new_tab(self):
        self.web_driver.execute_script('window.open()')
        tabs = self.web_driver.window_handles
        self.web_driver.switch_to.window(tabs[1])
