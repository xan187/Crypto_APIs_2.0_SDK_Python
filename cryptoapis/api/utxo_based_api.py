"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.api_client import ApiClient, Endpoint as _Endpoint
from cryptoapis.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cryptoapis.model.already_exists import AlreadyExists
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.get_hd_walletx_pub_y_pub_z_pub_details_response import GetHDWalletxPubYPubZPubDetailsResponse
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_xpub import InvalidXpub
from cryptoapis.model.list_hd_walletx_pub_y_pub_z_pub_transactions_response import ListHDWalletxPubYPubZPubTransactionsResponse
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.sync_hd_walletx_pub_y_pub_z_pub_request_body import SyncHDWalletxPubYPubZPubRequestBody
from cryptoapis.model.sync_hd_walletx_pub_y_pub_z_pub_response import SyncHDWalletxPubYPubZPubResponse
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
from cryptoapis.model.xpub_not_synced import XpubNotSynced
from cryptoapis.model.xpub_sync_in_progress import XpubSyncInProgress


class UTXOBasedApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_hd_wallet__x_pub_y_pub_z_pub_details(
            self,
            blockchain,
            extended_public_key,
            network,
            **kwargs
        ):
            """Get HD Wallet (xPub, yPub, zPub) Details  # noqa: E501

            HD wallet details is useful endpoint to get the most important data about HD wallet without the need to do a lot of calculations, once the HD Wallet is synced using Sync endpoint we keep it up to date and we calculate these details in advance.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_hd_wallet__x_pub_y_pub_z_pub_details(blockchain, extended_public_key, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                extended_public_key (str): Defines the account extended publicly known key which is used to derive all child public keys.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
                derivation (str): The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                GetHDWalletxPubYPubZPubDetailsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['blockchain'] = \
                blockchain
            kwargs['extended_public_key'] = \
                extended_public_key
            kwargs['network'] = \
                network
            return self.call_with_http_info(**kwargs)

        self.get_hd_wallet__x_pub_y_pub_z_pub_details = _Endpoint(
            settings={
                'response_type': (GetHDWalletxPubYPubZPubDetailsResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/details',
                'operation_id': 'get_hd_wallet__x_pub_y_pub_z_pub_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'extended_public_key',
                    'network',
                    'context',
                    'derivation',
                ],
                'required': [
                    'blockchain',
                    'extended_public_key',
                    'network',
                ],
                'nullable': [
                ],
                'enum': [
                    'blockchain',
                    'network',
                    'derivation',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('blockchain',): {

                        "BITCOIN": "bitcoin",
                        "BITCOIN-CASH": "bitcoin-cash",
                        "LITECOIN": "litecoin",
                        "DOGECOIN": "dogecoin",
                        "DASH": "dash"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet"
                    },
                    ('derivation',): {

                        "ACCOUNT": "account",
                        "BIP32": "bip32"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'extended_public_key':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'derivation':
                        (str,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'extended_public_key': 'extendedPublicKey',
                    'network': 'network',
                    'context': 'context',
                    'derivation': 'derivation',
                },
                'location_map': {
                    'blockchain': 'path',
                    'extended_public_key': 'path',
                    'network': 'path',
                    'context': 'query',
                    'derivation': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_hd_wallet__x_pub_y_pub_z_pub_details
        )

        def __list_hd_wallet__x_pub_y_pub_z_pub_transactions(
            self,
            blockchain,
            extended_public_key,
            network,
            **kwargs
        ):
            """List HD Wallet (xPub, yPub, zPub) Transactions  # noqa: E501

            This endpoint will list HD Wallet transactions.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_hd_wallet__x_pub_y_pub_z_pub_transactions(blockchain, extended_public_key, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain.
                extended_public_key (str): Defines the master public key (xPub) of the account.
                network (str): Represents the specific network.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
                derivation (str): The way how the HD walled derives, for example when the type is ACCOUNT, it derives change and receive addresses while when the type is BIP32 it derives directly.. [optional]
                limit (int): Defines how many items should be returned in the response per page basis.. [optional] if omitted the server will use the default value of 50
                offset (int): The starting index of the response items, i.e. where the response should start listing the returned items.. [optional] if omitted the server will use the default value of 0
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListHDWalletxPubYPubZPubTransactionsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['blockchain'] = \
                blockchain
            kwargs['extended_public_key'] = \
                extended_public_key
            kwargs['network'] = \
                network
            return self.call_with_http_info(**kwargs)

        self.list_hd_wallet__x_pub_y_pub_z_pub_transactions = _Endpoint(
            settings={
                'response_type': (ListHDWalletxPubYPubZPubTransactionsResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-data/{blockchain}/{network}/hd/{extendedPublicKey}/transactions',
                'operation_id': 'list_hd_wallet__x_pub_y_pub_z_pub_transactions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'extended_public_key',
                    'network',
                    'context',
                    'derivation',
                    'limit',
                    'offset',
                ],
                'required': [
                    'blockchain',
                    'extended_public_key',
                    'network',
                ],
                'nullable': [
                ],
                'enum': [
                    'blockchain',
                    'network',
                    'derivation',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('blockchain',): {

                        "BITCOIN": "bitcoin",
                        "BITCOIN-CASH": "bitcoin-cash",
                        "LITECOIN": "litecoin",
                        "DOGECOIN": "dogecoin",
                        "DASH": "dash"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet"
                    },
                    ('derivation',): {

                        "ACCOUNT": "account",
                        "BIP32": "bip32"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'extended_public_key':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'derivation':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'extended_public_key': 'extendedPublicKey',
                    'network': 'network',
                    'context': 'context',
                    'derivation': 'derivation',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'blockchain': 'path',
                    'extended_public_key': 'path',
                    'network': 'path',
                    'context': 'query',
                    'derivation': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_hd_wallet__x_pub_y_pub_z_pub_transactions
        )

        def __sync_hd_wallet__x_pub_y_pub_z_pub(
            self,
            blockchain,
            network,
            **kwargs
        ):
            """Sync HD Wallet (xPub, yPub, zPub)  # noqa: E501

            HD wallets usually have a lot of addresses and transactions, getting the data on demand is a heavy operation. That's why we have created this feature, to be able to get HD wallet details or transactions this HD wallet must be synced first. In addition to the initial sync we keep updating the synced HD wallets all the time.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.sync_hd_wallet__x_pub_y_pub_z_pub(blockchain, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
                sync_hd_walletx_pub_y_pub_z_pub_request_body (SyncHDWalletxPubYPubZPubRequestBody): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SyncHDWalletxPubYPubZPubResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['blockchain'] = \
                blockchain
            kwargs['network'] = \
                network
            return self.call_with_http_info(**kwargs)

        self.sync_hd_wallet__x_pub_y_pub_z_pub = _Endpoint(
            settings={
                'response_type': (SyncHDWalletxPubYPubZPubResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-data/{blockchain}/{network}/hd/sync',
                'operation_id': 'sync_hd_wallet__x_pub_y_pub_z_pub',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'context',
                    'sync_hd_walletx_pub_y_pub_z_pub_request_body',
                ],
                'required': [
                    'blockchain',
                    'network',
                ],
                'nullable': [
                ],
                'enum': [
                    'blockchain',
                    'network',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('blockchain',): {

                        "BITCOIN": "bitcoin",
                        "BITCOIN-CASH": "bitcoin-cash",
                        "LITECOIN": "litecoin",
                        "DOGECOIN": "dogecoin",
                        "DASH": "dash"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'sync_hd_walletx_pub_y_pub_z_pub_request_body':
                        (SyncHDWalletxPubYPubZPubRequestBody,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'network': 'network',
                    'context': 'context',
                },
                'location_map': {
                    'blockchain': 'path',
                    'network': 'path',
                    'context': 'query',
                    'sync_hd_walletx_pub_y_pub_z_pub_request_body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__sync_hd_wallet__x_pub_y_pub_z_pub
        )
