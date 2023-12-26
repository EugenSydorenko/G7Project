import logging
import os

from dotenv import load_dotenv

from api.common_actions_with_api import CommonActionsWithApi


class CoreApi(CommonActionsWithApi):

    def __init__(self):
        super().__init__()
        load_dotenv()
        self.core_url = os.environ.get('CORE_URL')
        core_token = os.environ.get('ECORE_TOKEN')
        self.headers = {'token': f'{core_token}'}

    def check_inventory_for_available_nodes(self) -> bool:
        api_url = self.core_url + '/inventories/available'
        response = self._call_api_get_response(api_url, self.headers)
        if len(response) == 0:
            logging.info('There is no free nodes')
            return False
        else:
            logging.info(response)  # for testing
            return True
