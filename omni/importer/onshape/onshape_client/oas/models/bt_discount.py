# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.108
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import sys  # noqa: F401

import six  # noqa: F401
from omni.importer.onshape.onshape_client.oas.model_utils import ModelNormal, datetime, int, str  # noqa: F401

try:
    from omni.importer.onshape.onshape_client.oas.models import bt_discount_owner_id_plan_id
except ImportError:
    bt_discount_owner_id_plan_id = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_discount_owner_id_plan_id"
    ]


class BTDiscount(ModelNormal):
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
            "id": (bt_discount_owner_id_plan_id.BTDiscountOwnerIdPlanId,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "description": (str,),  # noqa: E501
            "created_by": (str,),  # noqa: E501
            "created_at": (datetime,),  # noqa: E501
            "modified_by": (str,),  # noqa: E501
            "modified_at": (datetime,),  # noqa: E501
            "account_balance": (int,),  # noqa: E501
            "trial_end_date": (str,),  # noqa: E501
            "coupon_type": (int,),  # noqa: E501
            "coupon_valid_months": (int,),  # noqa: E501
            "percent_off": (int,),  # noqa: E501
            "amount_off": (int,),  # noqa: E501
            "amount_off_currency": (str,),  # noqa: E501
            "used_at": (datetime,),  # noqa: E501
            "expires_at": (datetime,),  # noqa: E501
            "new": (bool,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "id": "id",  # noqa: E501
        "name": "name",  # noqa: E501
        "description": "description",  # noqa: E501
        "created_by": "createdBy",  # noqa: E501
        "created_at": "createdAt",  # noqa: E501
        "modified_by": "modifiedBy",  # noqa: E501
        "modified_at": "modifiedAt",  # noqa: E501
        "account_balance": "accountBalance",  # noqa: E501
        "trial_end_date": "trialEndDate",  # noqa: E501
        "coupon_type": "couponType",  # noqa: E501
        "coupon_valid_months": "couponValidMonths",  # noqa: E501
        "percent_off": "percentOff",  # noqa: E501
        "amount_off": "amountOff",  # noqa: E501
        "amount_off_currency": "amountOffCurrency",  # noqa: E501
        "used_at": "usedAt",  # noqa: E501
        "expires_at": "expiresAt",  # noqa: E501
        "new": "new",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_discount.BTDiscount - a model defined in OpenAPI


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
            id (bt_discount_owner_id_plan_id.BTDiscountOwnerIdPlanId): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            modified_by (str): [optional]  # noqa: E501
            modified_at (datetime): [optional]  # noqa: E501
            account_balance (int): [optional]  # noqa: E501
            trial_end_date (str): [optional]  # noqa: E501
            coupon_type (int): [optional]  # noqa: E501
            coupon_valid_months (int): [optional]  # noqa: E501
            percent_off (int): [optional]  # noqa: E501
            amount_off (int): [optional]  # noqa: E501
            amount_off_currency (str): [optional]  # noqa: E501
            used_at (datetime): [optional]  # noqa: E501
            expires_at (datetime): [optional]  # noqa: E501
            new (bool): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
