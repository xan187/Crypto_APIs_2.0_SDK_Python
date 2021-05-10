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
from cryptoapis.model.coins_forwarding_automations_limit_reached import CoinsForwardingAutomationsLimitReached
from cryptoapis.model.create_automatic_coins_forwarding_request_body import CreateAutomaticCoinsForwardingRequestBody
from cryptoapis.model.create_automatic_coins_forwarding_response import CreateAutomaticCoinsForwardingResponse
from cryptoapis.model.delete_automatic_coins_forwarding_response import DeleteAutomaticCoinsForwardingResponse
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.list_coins_forwarding_automations_response import ListCoinsForwardingAutomationsResponse
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.resource_not_found import ResourceNotFound
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType


class AutomaticCoinsForwardingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_automatic_coins_forwarding(
            self,
            blockchain,
            network,
            **kwargs
        ):
            """Create Automatic Coins Forwarding  # noqa: E501

            Through this endpoint customers can set up an automatic forwarding function specifically for coins (**not** tokens). They can have a `toAddress` which is essentially the main address and the destination for the automatic coins forwarding.     There is also a `minimumTransferAmount` which only when reached will then trigger the forwarding. Through this the customer can save from fees.    Moreover, `feePriority` can be also set,  which defines how quickly to move the coins once they are received. The higher priority, the larger the fee will be. It can be \"SLOW\", \"STANDARD\" or \"FAST\".    The response of this endpoint contains an attribute `fromAddress` which can be used as a deposit address. Any funds received by this address will be automatically forwarded to `toAddress` based on what the customer has set for the automation.    For this automatic forwarding the customer can set a callback subscription.    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}    {note}This endpoint generates a new `fromAddress` each time.{/note}  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_automatic_coins_forwarding(blockchain, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
                create_automatic_coins_forwarding_request_body (CreateAutomaticCoinsForwardingRequestBody): [optional]
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
                CreateAutomaticCoinsForwardingResponse
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

        self.create_automatic_coins_forwarding = _Endpoint(
            settings={
                'response_type': (CreateAutomaticCoinsForwardingResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations',
                'operation_id': 'create_automatic_coins_forwarding',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'context',
                    'create_automatic_coins_forwarding_request_body',
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
                        "DASH": "dash",
                        "ETHEREUM": "ethereum",
                        "ETHEREUM-CLASSIC": "ethereum-classic"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "RINKEBY": "rinkeby",
                        "MORDOR": "mordor"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'create_automatic_coins_forwarding_request_body':
                        (CreateAutomaticCoinsForwardingRequestBody,),
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
                    'create_automatic_coins_forwarding_request_body': 'body',
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
            callable=__create_automatic_coins_forwarding
        )

        def __delete_automatic_coins_forwarding(
            self,
            blockchain,
            network,
            reference_id,
            **kwargs
        ):
            """Delete Automatic Coins Forwarding  # noqa: E501

            Through this endpoint customers can delete a forwarding function they have set for **coins** (**not** tokens).    By setting a `fromAddress` and a `toAddress`, and specifying the amount, coins can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_automatic_coins_forwarding(blockchain, network, reference_id, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.
                reference_id (str): Represents a unique ID used to reference the specific callback subscription.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
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
                DeleteAutomaticCoinsForwardingResponse
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
            kwargs['reference_id'] = \
                reference_id
            return self.call_with_http_info(**kwargs)

        self.delete_automatic_coins_forwarding = _Endpoint(
            settings={
                'response_type': (DeleteAutomaticCoinsForwardingResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations/{referenceId}',
                'operation_id': 'delete_automatic_coins_forwarding',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'reference_id',
                    'context',
                ],
                'required': [
                    'blockchain',
                    'network',
                    'reference_id',
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
                        "DASH": "dash",
                        "ETHEREUM": "ethereum",
                        "ETHEREUM-CLASSIC": "ethereum-classic"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "RINKEBY": "rinkeby",
                        "MORDOR": "mordor"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'reference_id':
                        (str,),
                    'context':
                        (str,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'network': 'network',
                    'reference_id': 'referenceId',
                    'context': 'context',
                },
                'location_map': {
                    'blockchain': 'path',
                    'network': 'path',
                    'reference_id': 'path',
                    'context': 'query',
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
            callable=__delete_automatic_coins_forwarding
        )

        def __list_coins_forwarding_automations(
            self,
            blockchain,
            network,
            **kwargs
        ):
            """List Coins Forwarding Automations  # noqa: E501

            Through this endpoint customers can list all of their **coins** forwarding automations (**not** tokens).    Customers can set up automatic forwarding functions for coins by setting a `fromAddress` and a `toAddress`, and specifying the amount that can be transferred between addresses.     A `feePriority` will be returned which represents the fee priority of the automation whether it is \"SLOW\", \"STANDARD\" OR \"FAST\".    {warning}The subscription will work for all incoming transactions until it is deleted. There is no need to do that for every transaction.{/warning}  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_coins_forwarding_automations(blockchain, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
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
                ListCoinsForwardingAutomationsResponse
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

        self.list_coins_forwarding_automations = _Endpoint(
            settings={
                'response_type': (ListCoinsForwardingAutomationsResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-automations/{blockchain}/{network}/coins-forwarding/automations',
                'operation_id': 'list_coins_forwarding_automations',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'context',
                    'limit',
                    'offset',
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
                        "DASH": "dash",
                        "ETHEREUM": "ethereum",
                        "ETHEREUM-CLASSIC": "ethereum-classic"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "RINKEBY": "rinkeby",
                        "MORDOR": "mordor"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'blockchain': 'blockchain',
                    'network': 'network',
                    'context': 'context',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'blockchain': 'path',
                    'network': 'path',
                    'context': 'query',
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
            callable=__list_coins_forwarding_automations
        )
