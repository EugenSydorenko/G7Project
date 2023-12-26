import unittest

from api.marketplace_api import MarketplaceApi


class MarketplaceApiTests(unittest.TestCase):
    marketplace_api = MarketplaceApi()

    def test_user_login(self):
        assert self.marketplace_api.user_login()

    def test_promo_code_validation(self):
        assert self.marketplace_api.check_promo_code_validation()

    def test_place_order(self):
        assert self.marketplace_api.place_order()

    def test_sign_up_new_user(self):
        assert self.marketplace_api.sign_up_new_user()
