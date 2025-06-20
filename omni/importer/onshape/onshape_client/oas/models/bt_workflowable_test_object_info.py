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
    from omni.importer.onshape.onshape_client.oas.models import bt_published_workflow_id
except ImportError:
    bt_published_workflow_id = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_published_workflow_id"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_workflow_property_info
except ImportError:
    bt_workflow_property_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_workflow_property_info"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_workflow_snapshot_info
except ImportError:
    bt_workflow_snapshot_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_workflow_snapshot_info"]


class BTWorkflowableTestObjectInfo(ModelNormal):
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
            "company_id": (str,),  # noqa: E501
            "description": (str,),  # noqa: E501
            "description_as_property": (str,),  # noqa: E501
            "document_id": (str,),  # noqa: E501
            "href": (str,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "info": ({str: (str,)},),  # noqa: E501
            "is_obsoletion": (bool,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "name_as_property": (str,),  # noqa: E501
            "properties": ([bt_workflow_property_info.BTWorkflowPropertyInfo],),  # noqa: E501
            "view_ref": (str,),  # noqa: E501
            "workflow": (bt_workflow_snapshot_info.BTWorkflowSnapshotInfo,),  # noqa: E501
            "workflow_id": (bt_published_workflow_id.BTPublishedWorkflowId,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "company_id": "companyId",  # noqa: E501
        "description": "description",  # noqa: E501
        "description_as_property": "descriptionAsProperty",  # noqa: E501
        "document_id": "documentId",  # noqa: E501
        "href": "href",  # noqa: E501
        "id": "id",  # noqa: E501
        "info": "info",  # noqa: E501
        "is_obsoletion": "isObsoletion",  # noqa: E501
        "name": "name",  # noqa: E501
        "name_as_property": "nameAsProperty",  # noqa: E501
        "properties": "properties",  # noqa: E501
        "view_ref": "viewRef",  # noqa: E501
        "workflow": "workflow",  # noqa: E501
        "workflow_id": "workflowId",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_workflowable_test_object_info.BTWorkflowableTestObjectInfo - a model defined in OpenAPI

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
            company_id (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            description_as_property (str): [optional]  # noqa: E501
            document_id (str): [optional]  # noqa: E501
            href (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            info ({str: (str,)}): [optional]  # noqa: E501
            is_obsoletion (bool): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            name_as_property (str): [optional]  # noqa: E501
            properties ([bt_workflow_property_info.BTWorkflowPropertyInfo]): [optional]  # noqa: E501
            view_ref (str): [optional]  # noqa: E501
            workflow (bt_workflow_snapshot_info.BTWorkflowSnapshotInfo): [optional]  # noqa: E501
            workflow_id (bt_published_workflow_id.BTPublishedWorkflowId): [optional]  # noqa: E501
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
