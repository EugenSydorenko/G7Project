import requests


class CoreApi:
    token = ''

    def __init__(self):


    def call_api_with_authorization(self):
        # Replace 'API_ENDPOINT_URL' with the actual API endpoint URL you want to call.
        api_url = 'API_ENDPOINT_URL'

        # Set the Authorization header with the class variable token.
        headers = {'Authorization': f'Bearer {self.token}'}

        try:
            # Make the API request with the headers.
            response = requests.get(api_url, headers=headers)

            # Check the response status code to handle different scenarios.
            if response.status_code == 200:
                # Request was successful.
                data = response.json()  # If the response is JSON, you can access the data using response.json()
                print('API response:', data)
            elif response.status_code == 401:
                # Unauthorized. The token might be invalid or expired.
                print('Unauthorized access. Please check your token.')
            else:
                # Other status codes. Handle the error accordingly.
                print('API request failed with status code:', response.status_code)
                print('Response content:', response.text)

        except requests.RequestException as e:
            print('Error occurred while making API request:', e)
