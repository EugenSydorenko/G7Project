import datetime
import logging
import os
import random

import requests
from dotenv import load_dotenv

from api.common_actions_with_api import CommonActionsWithApi


class MarketplaceApi(CommonActionsWithApi):

    def __init__(self):
        super().__init__()
        load_dotenv()
        self._marketplace_url = os.environ.get('MARKETPLACE_URL')
        self._valid_user_email = os.environ.get('USER_EMAIL_VALID')
        self._valid_user_password = os.environ.get('USER_PASSWORD')
        self._marketplace_token = self.__authenticate(self._marketplace_url, self._valid_user_email,
                                                      self._valid_user_password)

    @staticmethod
    def __authenticate(marketplace_url, valid_user_email, valid_user_password):
        endpoint_api_url = marketplace_url + '/user/login'
        data = {
            "username": f"{valid_user_email}",
            "password": f"{valid_user_password}",
            "remember_me": False
        }

        try:
            # Make the API request with the headers and data.
            response = requests.post(endpoint_api_url, json=data)

            # Check the response status code to handle different scenarios.
            if response.status_code == 200:
                response_data = response.json()
                token = response_data.get('token')
                if token:
                    return token
                else:
                    logging.info('Token not found in response')
            else:
                logging.info('API request failed with status code:', response.status_code)
                logging.info('Response content:', response.text)

        except requests.RequestException as e:
            logging.info('Error occurred while making API request:', e)

        return None  # Return None if authentication fails

    @staticmethod
    def __check_response(response, **expected_values):
        if response.status_code == 200:
            try:
                response_data = response.json()
            except ValueError:
                logging.error("Error decoding JSON response.")
                return False

            for key, expected_value in expected_values.items():
                if key not in response_data or response_data[key] != expected_value:
                    logging.info(f'Failed: {key} - Expected: {expected_value}, Actual: {response_data.get(key)}')
                    return False

            logging.info('Response:', response_data)
            return True
        else:
            logging.info('Response:', response.url, response.status_code, response.content)
            return False

    def __check_inventory_for_available_nodes(self) -> bool:
        api_url = self._marketplace_url + '/core-wrapper/inventories/available'
        headers = {'token': f'{self._marketplace_token}'}
        response = self._call_api_get_response(api_url, headers)
        if len(response) == 0:
            logging.info('There is no free nodes')
            return False
        else:
            logging.info(response)  # for testing
            return True

    def send_agent_action(self, action: str):
        expected_values = {
            'uuid': '3585f85e-3db1-4be6-b158-74aaad0eb8f0',
            'message': 'Action exection started.',
            'additional_key': 'additional_value',
        }
        uuid = expected_values.get('uuid')
        endpoint_api_url = self._marketplace_url + f'/agent/{uuid}/{action}'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self._marketplace_token}',
            'Content-Type': 'application/json'
        }
        data = {}  # Empty JSON data
        response = requests.post(endpoint_api_url, headers=headers, json=data)
        return self.__check_response(response, **expected_values)

    def user_login(self):
        endpoint_api_url = self._marketplace_url + '/user/login'
        headers = {
            'username': f'{self._valid_user_email}',
            'password': f'{self._valid_user_password}',
            'remember_me': False
        }
        expected_values = {
            'success': True,
            'message': 'Login Success...!'
        }
        data = {}  # Empty JSON data
        response = requests.post(endpoint_api_url, headers=headers, json=data)
        return self.__check_response(response, **expected_values)

    def check_promo_code_validation(self):
        endpoint_api_url = self._marketplace_url + '/core-wrapper/orders/get-promo'

        headers = {
            'email': f'{self._valid_user_email}',
            'server_service_id': 689,
            'blockchain_service_id': 3,
            'property_services': [
                4,
                1
            ],
            'code': 'EDUAT',
            'check_user': True
        }
        expected_values = {
            'is_valid': True,
            'total': 1.0
        }
        data = {}  # Empty JSON data
        response = requests.post(endpoint_api_url, headers=headers, json=data)
        return self.__check_response(response, **expected_values)

    def place_order(self):
        endpoint_api_url = self._marketplace_url + '/billings/whmcs/place-order'

        headers = {
            'payment_method': 'ecp',
            'property_services': [
                4,
                1
            ],
            'blockchain_service_id': 3,
            'server_service_id': 689,
            'promo_code': '',
            'is_agree_terms': True,
            'ssh_key': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCH3JI59q+2rJntpOSfvLgGu/RYnKE'
                       '/MnQZ2LOY1D1otWqDkyhDqycScMWHv9q7thFoE8RcgLgP48mblpkR7IgefhmTyjmXHOIPVnecOcULwCsAqm8N'
                       '+8z4uKF7KAzc76sNRXBePpci0u'
                       '/qzUiRaWzYqe6aSj8kO5VuyJiLY0Qr2TNWPInlQTwlKd1atGnE2rshnT16sHhxwOAA8PUCehIi5P2wpQ7ZsbT7r'
                       '/CauOotLgrO1tmoT51pklyDzxBwYhddDG4VESR6oEZ0jX4QxUzRTWzEgg20yd3CtEO6UHqETZUJVk3F8s8WWI8kW'
                       '/AqfXk6R140CAwQmTp7AU5pvcDB\n',
            'node_name': '1239',
            'install_agent': True,
            'cluster': 'devnet',
            'withdrawer_id': ''
        }

        data = {}  # Empty JSON data
        response = requests.post(endpoint_api_url, headers=headers, json=data)

        if response.content:
            return True
        else:
            logging.info('Response is empty.')
            return False

    @staticmethod
    def __add_random_digit(value):
        random_number = random.randint(0, 9)
        return value + str(random_number)

    @staticmethod
    def get_current_time_without_symbols() -> str:
        current_time = datetime.now()
        formatted_time = current_time.strftime('%H%M%S%d%m%Y')
        return formatted_time

    def check_and_modify_username(self, username: str):
        endpoint_api_url = self._marketplace_url + '/user/verify-username-or-email'

        # Make the initial API request with the provided username in the header
        headers = {'username': username}
        data = {}
        response = requests.get(endpoint_api_url, headers=headers, json=data)

        # Check the 'is_exists' field in the response
        if 'is_exists' in response and response['is_exists'] is False:
            # If 'is_exists' is False, return the original username
            return username
        elif 'is_exists' in response and response['is_exists'] is True:
            # If 'is_exists' is True, modify the username and check again
            modified_username = self.__add_random_digit(username)
            return self.check_and_modify_username(modified_username)
        else:
            logging.info('Unexpected response format.')
            return None

    def check_and_modify_email(self, email: str, plus_added: bool = False):
        endpoint_api_url = self._marketplace_url + '/user/verify-username-or-email'

        # Make the initial API request with the provided username in the header
        headers = {'username': email}
        data = {}
        response = requests.get(endpoint_api_url, headers=headers, json=data)

        # Check the 'is_exists' field in the response
        if 'is_exists' in response and response['is_exists'] is False:
            # If 'is_exists' is False, return the original email
            return email
        elif 'is_exists' in response and response['is_exists'] is True:
            # If 'is_exists' is True, modify the email and check again
            email_parts = email.split("@")
            modified_email = email_parts[0] + self.__class__.__add_random_digit() + "@" + email_parts[1]
            return self.check_and_modify_email(modified_email, plus_added=True)
        else:
            logging.info('Unexpected response format.')
            return None

    def sign_up_new_user(self):
        endpoint_api_url = self._marketplace_url + '/user/signup'
        current_date_time = self.get_current_time_without_symbols()
        username = 'E' + current_date_time
        email = (f'eugene.sydorenko ' + {current_date_time} + '@edgevana.com')

        headers = {
            "firstname": "Eugen",
            "lastname": "Sydorenko",
            "username": username,
            "email": email,
            "password": self._valid_user_password,
            "recaptcha_token": "03AFcWeA4S4ZWRZrjIqN_ZFJWBF7I0Wsns0XreO7f6bVYeQMFYxl2hCbH_7Pch9_sbVX5t6pSl-yiGRW26Mq_WjDORJo7vRxW2C3boeTl2joO_3Qk7VkwWSep6xNsTcAffPA-4_wdOKZ_xIPqpY8U4KRMbQF7RlaNFgq6VvKftQx51UKxLnHzXCU_CKUdQDHUUhD9NKxcSL5AmbiOQcVtcJP3p_QNDwlLPO2errfNZPUZI3bSGkDe_eqhJZBw2YJl5QT17Ph1Do2NApipR-8gRmY5GjdeOmVP13Ch-5b_-Wc_Cu6KUmNvXIPznSsZGgmC-7HKmCEA7C1uMMAcfggvwsIf0VNxY_mNHGa22Rda0_CvgokLAAIUs-PDjoxBCQXMuFkBMkHDkwy4lc9SY12GtTusfz1nTh3YWXv5SNMesQPc9qM86kxT8_RqtzTpSjrxPq3emkRvrKq0aVGz_7Ad_y4SwtoaNoD9XHqFSDuBPsr0h3Wi8ue4DT99qv7KaJOSLHpo-qnh_dR1DNy0w2TLFdrSojrLUeTNxG97MtxGaiMtEnlWB9mx_uD4IWMvz1PyftK_w7IOu8BiHZcwFhy8IuPIzggUd83aYkA",
            "account_type": "Individual",
            "company_name": "",
            "source": "",
            "referral": ""
        }

        expected_values = {
            'message': 'Signup Successfully'
        }

        data = {}  # Empty JSON data
        response = requests.post(endpoint_api_url, headers=headers, json=data)
        return self.__check_response(response, **expected_values)
