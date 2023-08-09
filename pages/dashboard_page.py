import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from pages.parent_page import ParentPage


class Dashboard(ParentPage):
    button_log_out = By.ID, 'Logout'
    button_add_node = By.ID, 'buttonAddNode'

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def __button_logout_element(self) -> WebElement:
        self.web_driver_wait_15.until(EC.element_to_be_clickable(self.web_driver.find_element(*self.button_log_out)))
        return self.web_driver.find_element(*self.button_log_out)

    def __button_add_node_element(self) -> WebElement:
        web_element: WebElement = self.find_element_with_waiting(self.button_add_node)
        return web_element

    def is_button_log_out_displayed(self) -> bool:
        button_log_out: WebElement = self.__button_logout_element()
        return self._is_element_displayed(button_log_out)

    def click_on_button_add_node(self):
        try:
            button_add_node: WebElement = self.__button_add_node_element()
            time.sleep(6)
            self._click_on_element(button_add_node)
        except TimeoutException:
            # Button doesn't exist, we were redirected to marketplace, do nothing
            pass

    def wait_for_end_of_deployment(self):
        max_wait_time = 1200
        button_text = 'Tour de Sun'
        start_time = time.time()

        while time.time() - start_time < max_wait_time:
            try:
                self.web_driver_wait_10.until(
                    EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{button_text}')]")))
                return True  # Element with text found
            except:
                pass
            time.sleep(10)  # Wait for 10 seconds before checking again

        return False  # Element with text not found within the time limit
