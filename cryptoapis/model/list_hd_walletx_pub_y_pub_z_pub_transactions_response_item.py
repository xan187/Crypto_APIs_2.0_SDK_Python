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
    from cryptoapis.model.list_hd_walletx_pub_y_pub_z_pub_transactions_response_item_fee import ListHDWalletxPubYPubZPubTransactionsResponseItemFee
    from cryptoapis.model.list_hd_walletx_pub_y_pub_z_pub_transactions_response_item_recipients import ListHDWalletxPubYPubZPubTransactionsResponseItemRecipients
    from cryptoapis.model.list_hd_walletx_pub_y_pub_z_pub_transactions_response_item_senders import ListHDWalletxPubYPubZPubTransactionsResponseItemSenders
    globals()['ListHDWalletxPubYPubZPubTransactionsResponseItemFee'] = ListHDWalletxPubYPubZPubTransactionsResponseItemFee
    globals()['ListHDWalletxPubYPubZPubTransactionsResponseItemRecipients'] = ListHDWalletxPubYPubZPubTransactionsResponseItemRecipients
    globals()['ListHDWalletxPubYPubZPubTransactionsResponseItemSenders'] = ListHDWalletxPubYPubZPubTransactionsResponseItemSenders


class ListHDWalletxPubYPubZPubTransactionsResponseItem(ModelNormal):
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

    additional_properties_type = None

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
            'index': (int,),  # noqa: E501
            'mined_in_block_hash': (str,),  # noqa: E501
            'mined_in_block_height': (int,),  # noqa: E501
            'recipients': ([ListHDWalletxPubYPubZPubTransactionsResponseItemRecipients],),  # noqa: E501
            'senders': ([ListHDWalletxPubYPubZPubTransactionsResponseItemSenders],),  # noqa: E501
            'timestamp': (int,),  # noqa: E501
            'transaction_hash': (str,),  # noqa: E501
            'transaction_id': (str,),  # noqa: E501
            'fee': (ListHDWalletxPubYPubZPubTransactionsResponseItemFee,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'index': 'index',  # noqa: E501
        'mined_in_block_hash': 'minedInBlockHash',  # noqa: E501
        'mined_in_block_height': 'minedInBlockHeight',  # noqa: E501
        'recipients': 'recipients',  # noqa: E501
        'senders': 'senders',  # noqa: E501
        'timestamp': 'timestamp',  # noqa: E501
        'transaction_hash': 'transactionHash',  # noqa: E501
        'transaction_id': 'transactionId',  # noqa: E501
        'fee': 'fee',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, index, mined_in_block_hash, mined_in_block_height, recipients, senders, timestamp, transaction_hash, transaction_id, fee, *args, **kwargs):  # noqa: E501
        """ListHDWalletxPubYPubZPubTransactionsResponseItem - a model defined in OpenAPI

        Args:
            index (int): Represents the index position of the transaction in the block.
            mined_in_block_hash (str): Represents the hash of the block where this transaction was mined/confirmed for first time. The hash is defined as a cryptographic digital fingerprint made by hashing the block header twice through the SHA256 algorithm.
            mined_in_block_height (int): Represents the hight of the block where this transaction was mined/confirmed for first time. The height is defined as the number of blocks in the blockchain preceding this specific block.
            recipients ([ListHDWalletxPubYPubZPubTransactionsResponseItemRecipients]): Represents a list of recipient addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list.
            senders ([ListHDWalletxPubYPubZPubTransactionsResponseItemSenders]): Represents a list of sender addresses with the respective amounts. In account-based protocols like Ethereum there is only one address in this list.
            timestamp (int): Defines the exact date/time in Unix Timestamp when this transaction was mined, confirmed or first seen in Mempool, if it is unconfirmed.
            transaction_hash (str): Represents the same as `transactionId` for account-based protocols like Ethereum, while it could be different in UTXO-based protocols like Bitcoin. E.g., in UTXO-based protocols `hash` is different from `transactionId` for SegWit transactions.
            transaction_id (str): Represents the unique identifier of a transaction, i.e. it could be `transactionId` in UTXO-based protocols like Bitcoin, and transaction `hash` in Ethereum blockchain.
            fee (ListHDWalletxPubYPubZPubTransactionsResponseItemFee):

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

        self.index = index
        self.mined_in_block_hash = mined_in_block_hash
        self.mined_in_block_height = mined_in_block_height
        self.recipients = recipients
        self.senders = senders
        self.timestamp = timestamp
        self.transaction_hash = transaction_hash
        self.transaction_id = transaction_id
        self.fee = fee
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
