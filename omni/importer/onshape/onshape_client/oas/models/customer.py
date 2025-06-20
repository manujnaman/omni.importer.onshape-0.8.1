# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.113
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from omni.importer.onshape.onshape_client.oas.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)

try:
    from omni.importer.onshape.onshape_client.oas.models import customer_card_collection
except ImportError:
    customer_card_collection = sys.modules["omni.importer.onshape.onshape_client.oas.models.customer_card_collection"]
try:
    from omni.importer.onshape.onshape_client.oas.models import customer_subscription_collection
except ImportError:
    customer_subscription_collection = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.customer_subscription_collection"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import discount
except ImportError:
    discount = sys.modules["omni.importer.onshape.onshape_client.oas.models.discount"]
try:
    from omni.importer.onshape.onshape_client.oas.models import external_account
except ImportError:
    external_account = sys.modules["omni.importer.onshape.onshape_client.oas.models.external_account"]
try:
    from omni.importer.onshape.onshape_client.oas.models import external_account_collection
except ImportError:
    external_account_collection = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.external_account_collection"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import next_recurring_charge
except ImportError:
    next_recurring_charge = sys.modules["omni.importer.onshape.onshape_client.oas.models.next_recurring_charge"]
try:
    from omni.importer.onshape.onshape_client.oas.models import shipping_details
except ImportError:
    shipping_details = sys.modules["omni.importer.onshape.onshape_client.oas.models.shipping_details"]
try:
    from omni.importer.onshape.onshape_client.oas.models import subscription
except ImportError:
    subscription = sys.modules["omni.importer.onshape.onshape_client.oas.models.subscription"]


class Customer(ModelNormal):
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

    allowed_values = {}

    validations = {}

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "account_balance": (int,),  # noqa: E501
            "business_vat_id": (str,),  # noqa: E501
            "cards": (customer_card_collection.CustomerCardCollection,),  # noqa: E501
            "created": (int,),  # noqa: E501
            "currency": (str,),  # noqa: E501
            "default_card": (str,),  # noqa: E501
            "default_source": (str,),  # noqa: E501
            "default_source_object": (external_account.ExternalAccount,),  # noqa: E501
            "deleted": (bool,),  # noqa: E501
            "delinquent": (bool,),  # noqa: E501
            "description": (str,),  # noqa: E501
            "discount": (discount.Discount,),  # noqa: E501
            "email": (str,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "livemode": (bool,),  # noqa: E501
            "metadata": ({str: (str,)},),  # noqa: E501
            "next_recurring_charge": (next_recurring_charge.NextRecurringCharge,),  # noqa: E501
            "object": (str,),  # noqa: E501
            "shipping": (shipping_details.ShippingDetails,),  # noqa: E501
            "sources": (external_account_collection.ExternalAccountCollection,),  # noqa: E501
            "subscription": (subscription.Subscription,),  # noqa: E501
            "subscriptions": (customer_subscription_collection.CustomerSubscriptionCollection,),  # noqa: E501
            "trial_end": (int,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "account_balance": "accountBalance",  # noqa: E501
        "business_vat_id": "businessVatId",  # noqa: E501
        "cards": "cards",  # noqa: E501
        "created": "created",  # noqa: E501
        "currency": "currency",  # noqa: E501
        "default_card": "defaultCard",  # noqa: E501
        "default_source": "defaultSource",  # noqa: E501
        "default_source_object": "defaultSourceObject",  # noqa: E501
        "deleted": "deleted",  # noqa: E501
        "delinquent": "delinquent",  # noqa: E501
        "description": "description",  # noqa: E501
        "discount": "discount",  # noqa: E501
        "email": "email",  # noqa: E501
        "id": "id",  # noqa: E501
        "livemode": "livemode",  # noqa: E501
        "metadata": "metadata",  # noqa: E501
        "next_recurring_charge": "nextRecurringCharge",  # noqa: E501
        "object": "object",  # noqa: E501
        "shipping": "shipping",  # noqa: E501
        "sources": "sources",  # noqa: E501
        "subscription": "subscription",  # noqa: E501
        "subscriptions": "subscriptions",  # noqa: E501
        "trial_end": "trialEnd",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """customer.Customer - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            account_balance (int): [optional]  # noqa: E501
            business_vat_id (str): [optional]  # noqa: E501
            cards (customer_card_collection.CustomerCardCollection): [optional]  # noqa: E501
            created (int): [optional]  # noqa: E501
            currency (str): [optional]  # noqa: E501
            default_card (str): [optional]  # noqa: E501
            default_source (str): [optional]  # noqa: E501
            default_source_object (external_account.ExternalAccount): [optional]  # noqa: E501
            deleted (bool): [optional]  # noqa: E501
            delinquent (bool): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            discount (discount.Discount): [optional]  # noqa: E501
            email (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            livemode (bool): [optional]  # noqa: E501
            metadata ({str: (str,)}): [optional]  # noqa: E501
            next_recurring_charge (next_recurring_charge.NextRecurringCharge): [optional]  # noqa: E501
            object (str): [optional]  # noqa: E501
            shipping (shipping_details.ShippingDetails): [optional]  # noqa: E501
            sources (external_account_collection.ExternalAccountCollection): [optional]  # noqa: E501
            subscription (subscription.Subscription): [optional]  # noqa: E501
            subscriptions (customer_subscription_collection.CustomerSubscriptionCollection): [optional]  # noqa: E501
            trial_end (int): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
