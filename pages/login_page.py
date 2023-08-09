from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.parent_page import ParentPage


class LoginPage(ParentPage):
    input_user_name_field = By.ID, 'validationCustom02'
    input_password_field = By.ID, 'validationCustom03'
    login_button = By.ID, 'buttonLogin'
    sign_up_button = By.ID, 'signUpLink'
    account_type_individual = By.XPATH, "//p[@class='head' and text()='Individual']"
    button_get_started = By.ID, 'buttonGetStarted'
    email_verification_message = By.XPATH, ('//p[contains(@class, "head") and contains(text(), "Please verify your '
                                            'email!")]')

    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.login_page_url = self.base_url + "/login"

    def __input_user_name_field_element(self) -> WebElement:
        web_element: WebElement = self.web_driver.find_element(*self.input_user_name_field)
        return web_element

    def __input_password_field_element(self) -> WebElement:
        input_password_field: WebElement = self.web_driver.find_element(*self.input_password_field)
        return input_password_field

    def __button_login_element(self) -> WebElement:
        button_login: WebElement = self.web_driver.find_element(*self.login_button)
        return button_login

    def __button_sign_up_element(self) -> WebElement:
        button_sign_up: WebElement = self.web_driver.find_element(*self.sign_up_button)
        return button_sign_up

    def __account_type_individual(self) -> WebElement:
        account_type_individual: WebElement = self.web_driver.find_element(*self.account_type_individual)
        return account_type_individual

    def __email_verification_message_element(self) -> WebElement:
        email_verification_message: WebElement = self.web_driver.find_element(*self.email_verification_message)
        return email_verification_message

    def __button_get_started_element(self) -> WebElement:
        button_get_started: WebElement = self.web_driver.find_element(*self.button_get_started)
        return button_get_started

    def open_login_page(self):
        try:
            self.web_driver.get(self.login_page_url)
            self.logger.info('\nLoginPage was opened')
            self.logger.info(self.login_page_url)
        except Exception as e:
            self.logger.error('Can not open Login page', e)
            assert False, 'Can not open Login page' + str(e)

    def enter_text_into_login_field(self, user_name: str):
        element: WebElement = self.__input_user_name_field_element()
        self._enter_text_into_element(element, user_name)

    def enter_text_into_password_field(self, password: str):
        element: WebElement = self.__input_password_field_element()
        self._enter_text_into_element(element, password)

    def click_on_button_login(self):
        button_login: WebElement = self.__button_login_element()
        self._click_on_element(button_login)

    def click_on_sign_up_button(self):
        sign_up_button: WebElement = self.__button_sign_up_element()
        self._click_on_element(sign_up_button)

    def click_on_account_type_individual(self):
        account_type_individual: WebElement = self.__account_type_individual()
        self._click_on_element(account_type_individual)

    def click_on_button_get_started(self):
        button_get_started: WebElement = self.__button_get_started_element()
        self._click_on_element(button_get_started)

    def is_email_verification_message_displayed(self) -> bool:
        email_verification_message: WebElement = self.find_element_with_waiting(self.email_verification_message)
        return self._is_element_displayed(email_verification_message)
