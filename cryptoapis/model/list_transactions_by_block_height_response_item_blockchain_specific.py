"""
    CryptoAPIs

    Crypto APIs 2.0 is a complex and innovative infrastructure layer that radically simplifies the development of any Blockchain and Crypto related applications. Organized around REST, Crypto APIs 2.0 can assist both novice Bitcoin/Ethereum enthusiasts and crypto experts with the development of their blockchain applications. Crypto APIs 2.0 provides unified endpoints and data, raw data, automatic tokens and coins forwardings, callback functionalities, and much more.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: developers@cryptoapis.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cryptoapis.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from cryptoapis.model.list_transactions_by_block_hash_response_item_blockchain_specific_bitcoin_cash_vin import ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVin
    from cryptoapis.model.list_transactions_by_block_hash_response_item_blockchain_specific_bitcoin_cash_vout import ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVout
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_bitcoin import ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoin
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_bitcoin_cash import ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoinCash
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_dash import ListTransactionsByBlockHeightResponseItemBlockchainSpecificDash
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_dogecoin import ListTransactionsByBlockHeightResponseItemBlockchainSpecificDogecoin
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_ethereum import ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereum
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_ethereum_classic import ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassic
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_ethereum_classic_gas_price import ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassicGasPrice
    from cryptoapis.model.list_transactions_by_block_height_response_item_blockchain_specific_litecoin import ListTransactionsByBlockHeightResponseItemBlockchainSpecificLitecoin
    globals()['ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVin'] = ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVin
    globals()['ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVout'] = ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVout
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoin'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoin
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoinCash'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoinCash
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificDash'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificDash
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificDogecoin'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificDogecoin
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereum'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereum
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassic'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassic
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassicGasPrice'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassicGasPrice
    globals()['ListTransactionsByBlockHeightResponseItemBlockchainSpecificLitecoin'] = ListTransactionsByBlockHeightResponseItemBlockchainSpecificLitecoin


class ListTransactionsByBlockHeightResponseItemBlockchainSpecific(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'locktime': (int,),  # noqa: E501
            'size': (int,),  # noqa: E501
            'v_size': (int,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'vin': ([ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVin],),  # noqa: E501
            'vout': ([ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVout],),  # noqa: E501
            'contract': (str,),  # noqa: E501
            'gas_limit': (str,),  # noqa: E501
            'gas_price': (ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassicGasPrice,),  # noqa: E501
            'gas_used': (str,),  # noqa: E501
            'input_data': (str,),  # noqa: E501
            'nonce': (str,),  # noqa: E501
            'transaction_status': (str,),  # noqa: E501
            'vsize': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'locktime': 'locktime',  # noqa: E501
        'size': 'size',  # noqa: E501
        'v_size': 'vSize',  # noqa: E501
        'version': 'version',  # noqa: E501
        'vin': 'vin',  # noqa: E501
        'vout': 'vout',  # noqa: E501
        'contract': 'contract',  # noqa: E501
        'gas_limit': 'gasLimit',  # noqa: E501
        'gas_price': 'gasPrice',  # noqa: E501
        'gas_used': 'gasUsed',  # noqa: E501
        'input_data': 'inputData',  # noqa: E501
        'nonce': 'nonce',  # noqa: E501
        'transaction_status': 'transactionStatus',  # noqa: E501
        'vsize': 'vsize',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ListTransactionsByBlockHeightResponseItemBlockchainSpecific - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            locktime (int): Represents the time at which a particular transaction can be added to the blockchain.. [optional]  # noqa: E501
            size (int): Represents the total size of this transaction.. [optional]  # noqa: E501
            v_size (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
            version (int): Represents the total size of this transaction.. [optional]  # noqa: E501
            vin ([ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVin]): Represents the transaction inputs.. [optional]  # noqa: E501
            vout ([ListTransactionsByBlockHashResponseItemBlockchainSpecificBitcoinCashVout]): Represents the transaction outputs.. [optional]  # noqa: E501
            contract (str): Represents the specific transaction contract.. [optional]  # noqa: E501
            gas_limit (str): Represents the amount of gas used by this specific transaction alone.. [optional]  # noqa: E501
            gas_price (ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassicGasPrice): [optional]  # noqa: E501
            gas_used (str): Represents the exact unit of gas that was used for the transaction.. [optional]  # noqa: E501
            input_data (str): Represents additional information that is required for the transaction.. [optional]  # noqa: E501
            nonce (str): Represents the sequential running number for an address, starting from 0 for the first transaction. E.g., if the nonce of a transaction is 10, it would be the 11th transaction sent from the sender's address.. [optional]  # noqa: E501
            transaction_status (str): Represents the status of this transaction.. [optional]  # noqa: E501
            vsize (int): Represents the virtual size of this transaction.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoin,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificBitcoinCash,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificDash,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificDogecoin,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereum,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificEthereumClassic,
              ListTransactionsByBlockHeightResponseItemBlockchainSpecificLitecoin,
          ],
        }
