import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.parent_page import ParentPage


class NewUserSignUpPage(ParentPage):
    error_message_for_existing_email = "//p[@class='error-message' and text()='User already exists with this email address']"
    error_message_for_existing_user_name = "//p[@class='error-message' and text()='Username is already taken']"
    user_first_name_field = By.ID, '1'
    user_last_name_field = By.ID, '2'
    user_user_name_field = By.ID, '3'
    user_email_field = By.ID, '4'
    user_password_field = By.ID, '5'
    user_confirm_password_field = By.ID, '6'
    button_sign_up = By.ID, 'buttonSignUp'

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def __user_first_name_field_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_first_name_field)
        return element

    def __user_last_name_field_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_last_name_field)
        return element

    def __input_user_user_name_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_user_name_field)
        return element

    def __user_email_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_email_field)
        return element

    def __input_user_password_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_password_field)
        return element

    def __input_user_confirm_password_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.user_confirm_password_field)
        return element

    def __button_sign_up_element(self) -> WebElement:
        element: WebElement = self.web_driver.find_element(*self.button_sign_up)
        return element

    def enter_into_user_first_name_field(self, first_name):
        user_first_name: WebElement = self.__user_first_name_field_element()
        self._enter_text_into_element(user_first_name, first_name)

    def enter_into_user_last_name_field(self, last_name):
        user_last_name: WebElement = self.__user_last_name_field_element()
        self._enter_text_into_element(user_last_name, last_name)

    def enter_into_user_name_field(self, user_name):
        user_name_field: WebElement = self.__input_user_user_name_element()
        self._enter_text_into_element(user_name_field, user_name)
        error_exists: bool = self.__check_error_message(self.error_message_for_existing_user_name)
        if error_exists:
            user_name += "+"
            while error_exists:
                user_name = self.__add_random_number(user_name)
                self.__input_user_user_name_element().clear()
                self.__input_user_user_name_element().send_keys(user_name)
                error_exists = self.__check_error_message(self.error_message_for_existing_user_name)
                if error_exists:
                    self.logger.info('User already exists with this user name: ' + user_name)

    def enter_into_user_email_field(self, email):
        user_email_field: WebElement = self.__user_email_element()
        self._enter_text_into_element(user_email_field, email)

        error_exists = self.__check_error_message(self.error_message_for_existing_email)
        if error_exists:
            email_parts = email.split("@")
            email_parts[0] += "+"
            while error_exists:
                modified_email = self.__add_random_number(email_parts[0]) + "@" + email_parts[1]
                self.__user_email_element().clear()
                self.__user_email_element().send_keys(modified_email)
                time.sleep(4)
                error_exists = self.__check_error_message(self.error_message_for_existing_email)
                if error_exists:
                    self.logger.info("User already exists with this email address: " + modified_email)
                email_parts = modified_email.split("@")

    def __check_error_message(self, error_message_xpath):
        try:
            element = self.web_driver.find_element(By.XPATH, error_message_xpath)
            return self._is_element_displayed(element)
        except Exception as e:
            return False  # Return False indicating that the error message is not displayed

    @staticmethod
    def __add_random_number(value):
        random_number = random.randint(0, 9)
        return value + str(random_number)

    def enter_into_user_password_field(self, password):
        user_password_field: WebElement = self.__input_user_password_element()
        self._enter_text_into_element(user_password_field, password)

    def enter_into_user_confirm_password(self, confirm_password: str):
        user_confirm_password_field: WebElement = self.__input_user_confirm_password_element()
        self._enter_text_into_element(user_confirm_password_field, confirm_password)

    def click_on_button_sign_up(self):
        button_sign_up: WebElement = self.__button_sign_up_element()
        self._click_on_element(button_sign_up)
