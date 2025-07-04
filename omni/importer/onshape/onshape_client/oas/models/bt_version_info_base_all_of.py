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
    from omni.importer.onshape.onshape_client.oas.models import bt_thumbnail_info
except ImportError:
    bt_thumbnail_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_thumbnail_info"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_user_basic_summary_info
except ImportError:
    bt_user_basic_summary_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_user_basic_summary_info"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_version_info
except ImportError:
    bt_version_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_version_info"]


class BTVersionInfoBaseAllOf(ModelNormal):
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
            "created_at": (datetime,),  # noqa: E501
            "creator": (bt_user_basic_summary_info.BTUserBasicSummaryInfo,),  # noqa: E501
            "description": (str,),  # noqa: E501
            "document_id": (str,),  # noqa: E501
            "last_modifier": (bt_user_basic_summary_info.BTUserBasicSummaryInfo,),  # noqa: E501
            "microversion": (str,),  # noqa: E501
            "modified_at": (datetime,),  # noqa: E501
            "override_date": (datetime,),  # noqa: E501
            "parent": (str,),  # noqa: E501
            "parents": ([bt_version_info.BTVersionInfo],),  # noqa: E501
            "thumbnail": (bt_thumbnail_info.BTThumbnailInfo,),  # noqa: E501
            "type": (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "created_at": "createdAt",  # noqa: E501
        "creator": "creator",  # noqa: E501
        "description": "description",  # noqa: E501
        "document_id": "documentId",  # noqa: E501
        "last_modifier": "lastModifier",  # noqa: E501
        "microversion": "microversion",  # noqa: E501
        "modified_at": "modifiedAt",  # noqa: E501
        "override_date": "overrideDate",  # noqa: E501
        "parent": "parent",  # noqa: E501
        "parents": "parents",  # noqa: E501
        "thumbnail": "thumbnail",  # noqa: E501
        "type": "type",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_version_info_base_all_of.BTVersionInfoBaseAllOf - a model defined in OpenAPI

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
            created_at (datetime): [optional]  # noqa: E501
            creator (bt_user_basic_summary_info.BTUserBasicSummaryInfo): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            document_id (str): [optional]  # noqa: E501
            last_modifier (bt_user_basic_summary_info.BTUserBasicSummaryInfo): [optional]  # noqa: E501
            microversion (str): [optional]  # noqa: E501
            modified_at (datetime): [optional]  # noqa: E501
            override_date (datetime): [optional]  # noqa: E501
            parent (str): [optional]  # noqa: E501
            parents ([bt_version_info.BTVersionInfo]): [optional]  # noqa: E501
            thumbnail (bt_thumbnail_info.BTThumbnailInfo): [optional]  # noqa: E501
            type (str): [optional]  # noqa: E501
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
