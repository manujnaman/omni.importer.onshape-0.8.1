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


class BTDocumentSearchParams(ModelNormal):
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
        ("found_in",): {"ALL": "ALL", "WORKSPACES": "WORKSPACES", "VERSIONS": "VERSIONS"},
        ("when",): {"ALL": "ALL", "LATEST": "LATEST", "LATEST_PER_HIT": "LATEST_PER_HIT"},
    }

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
            "document_filter": (int,),  # noqa: E501
            "found_in": (str,),  # noqa: E501
            "limit": (int,),  # noqa: E501
            "offset": (int,),  # noqa: E501
            "owner_id": (str,),  # noqa: E501
            "parent_id": (str,),  # noqa: E501
            "raw_query": (str,),  # noqa: E501
            "sort_column": (str,),  # noqa: E501
            "sort_order": (str,),  # noqa: E501
            "type": (str,),  # noqa: E501
            "when": (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "document_filter": "documentFilter",  # noqa: E501
        "found_in": "foundIn",  # noqa: E501
        "limit": "limit",  # noqa: E501
        "offset": "offset",  # noqa: E501
        "owner_id": "ownerId",  # noqa: E501
        "parent_id": "parentId",  # noqa: E501
        "raw_query": "rawQuery",  # noqa: E501
        "sort_column": "sortColumn",  # noqa: E501
        "sort_order": "sortOrder",  # noqa: E501
        "type": "type",  # noqa: E501
        "when": "when",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_document_search_params.BTDocumentSearchParams - a model defined in OpenAPI

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
            document_filter (int): [optional]  # noqa: E501
            found_in (str): [optional]  # noqa: E501
            limit (int): [optional]  # noqa: E501
            offset (int): [optional]  # noqa: E501
            owner_id (str): [optional]  # noqa: E501
            parent_id (str): [optional]  # noqa: E501
            raw_query (str): [optional]  # noqa: E501
            sort_column (str): [optional]  # noqa: E501
            sort_order (str): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
            when (str): [optional]  # noqa: E501
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
