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
    from omni.importer.onshape.onshape_client.oas.models import btp_annotation231
except ImportError:
    btp_annotation231 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_annotation231"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_argument_declaration232
except ImportError:
    btp_argument_declaration232 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.btp_argument_declaration232"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_builtin_identifier233
except ImportError:
    btp_builtin_identifier233 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_builtin_identifier233"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_literal_map_entry257
except ImportError:
    btp_literal_map_entry257 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_literal_map_entry257"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_module234
except ImportError:
    btp_module234 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_module234"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_module_id235
except ImportError:
    btp_module_id235 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_module_id235"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_name261
except ImportError:
    btp_name261 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_name261"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_property_accessor23
except ImportError:
    btp_property_accessor23 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_property_accessor23"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_space10
except ImportError:
    btp_space10 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_space10"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_statement269
except ImportError:
    btp_statement269 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_statement269"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_top_level_node286
except ImportError:
    btp_top_level_node286 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_top_level_node286"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btp_type_name290
except ImportError:
    btp_type_name290 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btp_type_name290"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btpl_value249
except ImportError:
    btpl_value249 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btpl_value249"]


class BTPNode7(ModelNormal):
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
        ("documentation_type",): {
            "FUNCTION": "FUNCTION",
            "PREDICATE": "PREDICATE",
            "CONSTANT": "CONSTANT",
            "ENUM": "ENUM",
            "USER_TYPE": "USER_TYPE",
            "FEATURE_DEFINITION": "FEATURE_DEFINITION",
            "FILE_HEADER": "FILE_HEADER",
            "UNDOCUMENTABLE": "UNDOCUMENTABLE",
            "UNKNOWN": "UNKNOWN",
        }
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
            "atomic": (bool,),  # noqa: E501
            "bt_type": (str,),  # noqa: E501
            "documentation_type": (str,),  # noqa: E501
            "end_source_location": (int,),  # noqa: E501
            "node_id": (str,),  # noqa: E501
            "short_descriptor": (str,),  # noqa: E501
            "space_after": (btp_space10.BTPSpace10,),  # noqa: E501
            "space_before": (btp_space10.BTPSpace10,),  # noqa: E501
            "space_default": (bool,),  # noqa: E501
            "start_source_location": (int,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return {
            "bt_type": {
                "BTPTopLevelNode-286": btp_top_level_node286.BTPTopLevelNode286,
                "BTPStatement-269": btp_statement269.BTPStatement269,
                "BTPPropertyAccessor-23": btp_property_accessor23.BTPPropertyAccessor23,
                "BTPTypeName-290": btp_type_name290.BTPTypeName290,
                "BTPModule-234": btp_module234.BTPModule234,
                "BTPLValue-249": btpl_value249.BTPLValue249,
                "BTPBuiltinIdentifier-233": btp_builtin_identifier233.BTPBuiltinIdentifier233,
                "BTPName-261": btp_name261.BTPName261,
                "BTPLiteralMapEntry-257": btp_literal_map_entry257.BTPLiteralMapEntry257,
                "BTPArgumentDeclaration-232": btp_argument_declaration232.BTPArgumentDeclaration232,
                "BTPModuleId-235": btp_module_id235.BTPModuleId235,
            }
        }

    attribute_map = {
        "atomic": "atomic",  # noqa: E501
        "bt_type": "btType",  # noqa: E501
        "documentation_type": "documentationType",  # noqa: E501
        "end_source_location": "endSourceLocation",  # noqa: E501
        "node_id": "nodeId",  # noqa: E501
        "short_descriptor": "shortDescriptor",  # noqa: E501
        "space_after": "spaceAfter",  # noqa: E501
        "space_before": "spaceBefore",  # noqa: E501
        "space_default": "spaceDefault",  # noqa: E501
        "start_source_location": "startSourceLocation",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """btp_node7.BTPNode7 - a model defined in OpenAPI

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
            atomic (bool): [optional]  # noqa: E501
            bt_type (str): [optional]  # noqa: E501
            documentation_type (str): [optional]  # noqa: E501
            end_source_location (int): [optional]  # noqa: E501
            node_id (str): [optional]  # noqa: E501
            short_descriptor (str): [optional]  # noqa: E501
            space_after (btp_space10.BTPSpace10): [optional]  # noqa: E501
            space_before (btp_space10.BTPSpace10): [optional]  # noqa: E501
            space_default (bool): [optional]  # noqa: E501
            start_source_location (int): [optional]  # noqa: E501
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

    @classmethod
    def get_discriminator_class(cls, from_server, data):
        """Returns the child class specified by the discriminator"""
        discriminator = cls.discriminator()
        discr_propertyname_py = list(discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if from_server:
            class_name = data[discr_propertyname_js]
        else:
            class_name = data[discr_propertyname_py]
        class_name_to_discr_class = discriminator[discr_propertyname_py]
        return class_name_to_discr_class.get(class_name)
