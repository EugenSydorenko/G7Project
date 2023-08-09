import os

import requests
from dotenv import load_dotenv

from api.common_actions_with_api import CommonActionsWithApi


class MarketplaceApi(CommonActionsWithApi):

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.marketplace_url = os.environ.get('MARKETPLACE_URL')
        self.marketplace_token = self.__authenticate(self.marketplace_url)

    @staticmethod
    def __authenticate(marketplace_url):
        api_url = marketplace_url + '/user/login'
        valid_user_email = os.environ.get('USER_EMAIL_VALID')
        user_password = os.environ.get('USER_PASSWORD')
        data = {
            "username": f"{valid_user_email}",
            "password": f"{user_password}",
            "remember_me": False
        }

        try:
            # Make the API request with the headers and data.
            response = requests.post(api_url, json=data)

            # Check the response status code to handle different scenarios.
            if response.status_code == 200:
                response_data = response.json()
                token = response_data.get('token')
                if token:
                    return token
                else:
                    print('Token not found in response')
            else:
                print('API request failed with status code:', response.status_code)
                print('Response content:', response.text)

        except requests.RequestException as e:
            print('Error occurred while making API request:', e)

        return None  # Return None if authentication fails

    # /agent/{uuid}/{action}
    uuid: str = '39d4779c-72f7-4240-87e1-fd8418acb447'
    success_message: str = 'Action exection started.'

    def send_agent_action(self, action: str):
        api_url = self.marketplace_url + f'/agent/{self.uuid}/{action}'
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.marketplace_token}',
            'Content-Type': 'application/json'
        }
        data = {}  # Empty JSON data
        response = requests.post(api_url, headers=headers, json=data)
        return self.__check_response(response)

    def __check_response(self, response):
        if response.status_code == 200:
            response_data = response.json()
            if 'uuid' in response_data and 'message' in response_data:
                if response_data['message'] == self.success_message:
                    print('Response:', response_data)
                    return True
                else:
                    print('Response does not match expected data.')
                    return False
            else:
                print('Response is missing expected keys.')
                return False
        else:
            print('Response:', response.url, response.status_code, response.content)
            return False
