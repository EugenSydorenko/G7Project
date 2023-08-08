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
        self.headers = {'token': f'{self.marketplace_token}'}

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
