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
from cryptoapis.model.feature_mainnets_not_allowed_for_plan import FeatureMainnetsNotAllowedForPlan
from cryptoapis.model.insufficient_credits import InsufficientCredits
from cryptoapis.model.invalid_api_key import InvalidApiKey
from cryptoapis.model.invalid_data import InvalidData
from cryptoapis.model.invalid_pagination import InvalidPagination
from cryptoapis.model.invalid_request_body_structure import InvalidRequestBodyStructure
from cryptoapis.model.request_limit_reached import RequestLimitReached
from cryptoapis.model.unexpected_server_error import UnexpectedServerError
from cryptoapis.model.unsupported_media_type import UnsupportedMediaType
from cryptoapis.model.validate_address_request_body import ValidateAddressRequestBody
from cryptoapis.model.validate_address_response import ValidateAddressResponse


class ValidatingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __validate_address(
            self,
            blockchain,
            network,
            **kwargs
        ):
            """Validate Address  # noqa: E501

            This endpoint checks user public addresses whether they are valid or not.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.validate_address(blockchain, network, async_req=True)
            >>> result = thread.get()

            Args:
                blockchain (str): Represents the specific blockchain protocol name, e.g. Ethereum, Bitcoin, etc.
                network (str): Represents the name of the blockchain network used; blockchain networks are usually identical as technology and software, but they differ in data, e.g. - \"mainnet\" is the live network with actual data while networks like \"testnet\", \"ropsten\", \"rinkeby\" are test networks.

            Keyword Args:
                context (str): In batch situations the user can use the context to correlate responses with requests. This property is present regardless of whether the response was successful or returned as an error. `context` is specified by the user.. [optional]
                validate_address_request_body (ValidateAddressRequestBody): [optional]
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
                ValidateAddressResponse
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

        self.validate_address = _Endpoint(
            settings={
                'response_type': (ValidateAddressResponse,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/blockchain-tools/{blockchain}/{network}/addresses/validate',
                'operation_id': 'validate_address',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'blockchain',
                    'network',
                    'context',
                    'validate_address_request_body',
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
                        "ETHEREUM-CLASSIC": "ethereum-classic",
                        "XRP": "xrp"
                    },
                    ('network',): {

                        "MAINNET": "mainnet",
                        "TESTNET": "testnet",
                        "ROPSTEN": "ropsten",
                        "RINKEBY": "rinkeby",
                        "MORDOR": "mordor",
                        "KOTTI": "kotti"
                    },
                },
                'openapi_types': {
                    'blockchain':
                        (str,),
                    'network':
                        (str,),
                    'context':
                        (str,),
                    'validate_address_request_body':
                        (ValidateAddressRequestBody,),
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
                    'validate_address_request_body': 'body',
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
            callable=__validate_address
        )
