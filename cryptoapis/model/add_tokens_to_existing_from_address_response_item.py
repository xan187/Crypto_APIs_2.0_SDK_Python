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
    from cryptoapis.model.add_tokens_to_existing_from_address_response_item_token_data import AddTokensToExistingFromAddressResponseItemTokenData
    globals()['AddTokensToExistingFromAddressResponseItemTokenData'] = AddTokensToExistingFromAddressResponseItemTokenData


class AddTokensToExistingFromAddressResponseItem(ModelNormal):
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
        ('fee_priority',): {
            'SLOW': "slow",
            'STANDARD': "standard",
            'FAST': "fast",
        },
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
            'callback_url': (str,),  # noqa: E501
            'confirmations_count': (int,),  # noqa: E501
            'created_timestamp': (int,),  # noqa: E501
            'fee_address': (str,),  # noqa: E501
            'fee_priority': (str,),  # noqa: E501
            'from_address': (str,),  # noqa: E501
            'minimum_transfer_amount': (str,),  # noqa: E501
            'reference_id': (str,),  # noqa: E501
            'to_address': (str,),  # noqa: E501
            'token_data': (AddTokensToExistingFromAddressResponseItemTokenData,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'callback_url': 'callbackUrl',  # noqa: E501
        'confirmations_count': 'confirmationsCount',  # noqa: E501
        'created_timestamp': 'createdTimestamp',  # noqa: E501
        'fee_address': 'feeAddress',  # noqa: E501
        'fee_priority': 'feePriority',  # noqa: E501
        'from_address': 'fromAddress',  # noqa: E501
        'minimum_transfer_amount': 'minimumTransferAmount',  # noqa: E501
        'reference_id': 'referenceId',  # noqa: E501
        'to_address': 'toAddress',  # noqa: E501
        'token_data': 'tokenData',  # noqa: E501
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
    def __init__(self, callback_url, confirmations_count, created_timestamp, fee_address, fee_priority, from_address, minimum_transfer_amount, reference_id, to_address, token_data, *args, **kwargs):  # noqa: E501
        """AddTokensToExistingFromAddressResponseItem - a model defined in OpenAPI

        Args:
            callback_url (str): Represents the URL that is set by the customer where the callback will be received at. The callback notification will be received only if and when the event occurs.
            confirmations_count (int): Represents the number of confirmations, i.e. the amount of blocks that have been built on top of this block.
            created_timestamp (int): Defines the specific time/date when the automatic forwarding was created in Unix Timestamp.
            fee_address (str): Represents the specific fee address, which is always automatically generated. Users must fund it.
            fee_priority (str): Represents the fee priority of the automation, whether it is \"SLOW\", \"STANDARD\" or \"FAST\".
            from_address (str): Represents the hash of the address that forwards the tokens.
            minimum_transfer_amount (str): Represents the minimum transfer amount of the tokens in the `fromAddress` that can be allowed for an automatic forwarding.
            reference_id (str): Represents a unique ID used to reference the specific callback subscription.
            to_address (str): Represents the hash of the address the tokens are forwarded to.
            token_data (AddTokensToExistingFromAddressResponseItemTokenData):

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

        self.callback_url = callback_url
        self.confirmations_count = confirmations_count
        self.created_timestamp = created_timestamp
        self.fee_address = fee_address
        self.fee_priority = fee_priority
        self.from_address = from_address
        self.minimum_transfer_amount = minimum_transfer_amount
        self.reference_id = reference_id
        self.to_address = to_address
        self.token_data = token_data
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
