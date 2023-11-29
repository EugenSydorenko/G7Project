import unittest

from api.marketplace_api import MarketplaceApi


class MarketplaceApiTests(unittest.TestCase):
    marketplace_api = MarketplaceApi()

    def test_agent_action_solana_info(self):
        assert self.marketplace_api.send_agent_action('solana_info')

    def test_agent_action_server_specifications(self):
        assert self.marketplace_api.send_agent_action('server_specifications')

    def test_agent_action_os_uptime(self):
        assert self.marketplace_api.send_agent_action('os_uptime')

    def test_agent_action_node_uptime(self):
        assert self.marketplace_api.send_agent_action('node_uptime')

    def test_agent_action_os_usage(self):
        assert self.marketplace_api.send_agent_action('os_usage')

    def test_agent_action_reinstall(self):
        assert self.marketplace_api.send_agent_action('reinstall')

    def test_agent_action_ufw_status(self):
        assert self.marketplace_api.send_agent_action('ufw_status')
