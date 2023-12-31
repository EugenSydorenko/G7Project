import requests
import logging


class CommonActionsWithApi:
    def __init__(self):
        pass

    @staticmethod
    def _call_api_get_response(api_url, headers):
        try:
            # Make the API request with the headers.
            response = requests.get(api_url, headers=headers)

            # Check the response status code to handle different scenarios.
            if response.status_code == 200:
                # Request was successful.
                data = response.json()  # If the response is JSON, you can access the data using response.json()
                return data
            elif response.status_code == 401:
                # Unauthorized. The token might be invalid or expired.
                logging.error('Unauthorized access. Please check your token.')
            else:
                # Other status codes. Handle the error accordingly.
                logging.info('API request failed with status code:', response.status_code)
                logging.info('Response content:', response.text)

        except requests.RequestException as e:
            logging.info('Error occurred while making API request:', e)
