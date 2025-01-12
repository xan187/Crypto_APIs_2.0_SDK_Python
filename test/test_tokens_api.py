"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import cryptoapis
from cryptoapis.api.tokens_api import TokensApi  # noqa: E501


class TestTokensApi(unittest.TestCase):
    """TokensApi unit test stubs"""

    def setUp(self):
        self.api = TokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_tokens_by_address(self):
        """Test case for list_tokens_by_address

        List Tokens By Address  # noqa: E501
        """
        pass

    def test_list_tokens_transfers_by_address(self):
        """Test case for list_tokens_transfers_by_address

        List Tokens Transfers By Address  # noqa: E501
        """
        pass

    def test_list_tokens_transfers_by_transaction_hash(self):
        """Test case for list_tokens_transfers_by_transaction_hash

        List Tokens Transfers By Transaction Hash  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
