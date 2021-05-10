"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.xrp__ripple_api import XRPRippleApi  # noqa: E501


class TestXRPRippleApi(unittest.TestCase):
    """XRPRippleApi unit test stubs"""

    def setUp(self):
        self.api = XRPRippleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_latest_mined_xrp__ripple_block(self):
        """Test case for get_latest_mined_xrp__ripple_block

        Get Latest Mined XRP (Ripple) Block  # noqa: E501
        """
        pass

    def test_get_xrp__ripple_address_details(self):
        """Test case for get_xrp__ripple_address_details

        Get XRP (Ripple) Address Details  # noqa: E501
        """
        pass

    def test_get_xrp__ripple_block_details_by_block_hash(self):
        """Test case for get_xrp__ripple_block_details_by_block_hash

        Get XRP (Ripple) Block Details By Block Hash  # noqa: E501
        """
        pass

    def test_get_xrp__ripple_block_details_by_block_height(self):
        """Test case for get_xrp__ripple_block_details_by_block_height

        Get XRP (Ripple) Block Details By Block Height  # noqa: E501
        """
        pass

    def test_get_xrp__ripple_transaction_details_by_transaction_id(self):
        """Test case for get_xrp__ripple_transaction_details_by_transaction_id

        Get XRP (Ripple) Transaction Details By Transaction ID  # noqa: E501
        """
        pass

    def test_list_xrp__ripple_transactions_by_address(self):
        """Test case for list_xrp__ripple_transactions_by_address

        List XRP (Ripple) Transactions by Address  # noqa: E501
        """
        pass

    def test_list_xrp__ripple_transactions_by_block_hash(self):
        """Test case for list_xrp__ripple_transactions_by_block_hash

        List XRP (Ripple) Transactions By Block Hash  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
