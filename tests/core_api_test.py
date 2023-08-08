import unittest

from api.core_api import CoreApi
from api.marketplace_api import MarketplaceApi


class CoreApiTest(unittest.TestCase):
    def test_available_inventory(self):
        core_api = CoreApi()
        core_api.check_inventory_for_available_nodes()
        assert True

    def test_marketplace_api(self):
        marketplace_api = MarketplaceApi()
        print(marketplace_api.authenticate())
        assert True

    # agent api tests
    # https://edgevana.atlassian.net/wiki/spaces/ETD/pages/438992897/Proposal+for+Transitioning+to+Microservices+Architecture#Agent.1
