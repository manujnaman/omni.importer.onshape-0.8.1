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
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_appearance1740
except ImportError:
    bt_parameter_spec_appearance1740 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_appearance1740"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_array2600
except ImportError:
    bt_parameter_spec_array2600 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_array2600"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_boolean170
except ImportError:
    bt_parameter_spec_boolean170 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_boolean170"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_database1071
except ImportError:
    bt_parameter_spec_database1071 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_database1071"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_derived736
except ImportError:
    bt_parameter_spec_derived736 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_derived736"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_enum171
except ImportError:
    bt_parameter_spec_enum171 = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_enum171"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_feature_list703
except ImportError:
    bt_parameter_spec_feature_list703 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_feature_list703"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_foreign_id172
except ImportError:
    bt_parameter_spec_foreign_id172 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_foreign_id172"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_lookup_table_path761
except ImportError:
    bt_parameter_spec_lookup_table_path761 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_lookup_table_path761"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_material2700
except ImportError:
    bt_parameter_spec_material2700 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_material2700"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_nullable_quantity715
except ImportError:
    bt_parameter_spec_nullable_quantity715 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_nullable_quantity715"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_quantity173
except ImportError:
    bt_parameter_spec_quantity173 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_quantity173"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_query174
except ImportError:
    bt_parameter_spec_query174 = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_query174"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_reference2789
except ImportError:
    bt_parameter_spec_reference2789 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_reference2789"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_spec_string175
except ImportError:
    bt_parameter_spec_string175 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_spec_string175"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_parameter_visibility_condition177
except ImportError:
    bt_parameter_visibility_condition177 = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_parameter_visibility_condition177"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import btm_parameter1
except ImportError:
    btm_parameter1 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btm_parameter1"]


class BTParameterSpec6(ModelNormal):
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
        ("ui_hints",): {
            "OPPOSITE_DIRECTION": "OPPOSITE_DIRECTION",
            "ALWAYS_HIDDEN": "ALWAYS_HIDDEN",
            "SHOW_CREATE_SELECTION": "SHOW_CREATE_SELECTION",
            "CONTROL_VISIBILITY": "CONTROL_VISIBILITY",
            "NO_PREVIEW_PROVIDED": "NO_PREVIEW_PROVIDED",
            "REMEMBER_PREVIOUS_VALUE": "REMEMBER_PREVIOUS_VALUE",
            "DISPLAY_SHORT": "DISPLAY_SHORT",
            "ALLOW_FEATURE_SELECTION": "ALLOW_FEATURE_SELECTION",
            "MATE_CONNECTOR_AXIS_TYPE": "MATE_CONNECTOR_AXIS_TYPE",
            "PRIMARY_AXIS": "PRIMARY_AXIS",
            "SHOW_EXPRESSION": "SHOW_EXPRESSION",
            "OPPOSITE_DIRECTION_CIRCULAR": "OPPOSITE_DIRECTION_CIRCULAR",
            "SHOW_LABEL": "SHOW_LABEL",
            "HORIZONTAL_ENUM": "HORIZONTAL_ENUM",
            "UNCONFIGURABLE": "UNCONFIGURABLE",
            "MATCH_LAST_ARRAY_ITEM": "MATCH_LAST_ARRAY_ITEM",
            "COLLAPSE_ARRAY_ITEMS": "COLLAPSE_ARRAY_ITEMS",
            "INITIAL_FOCUS_ON_EDIT": "INITIAL_FOCUS_ON_EDIT",
            "INITIAL_FOCUS": "INITIAL_FOCUS",
            "DISPLAY_CURRENT_VALUE_ONLY": "DISPLAY_CURRENT_VALUE_ONLY",
            "READ_ONLY": "READ_ONLY",
            "PREVENT_CREATING_NEW_MATE_CONNECTORS": "PREVENT_CREATING_NEW_MATE_CONNECTORS",
            "FIRST_IN_ROW": "FIRST_IN_ROW",
            "ALLOW_QUERY_ORDER": "ALLOW_QUERY_ORDER",
            "PREVENT_ARRAY_REORDER": "PREVENT_ARRAY_REORDER",
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
            "additional_localized_strings": (int,),  # noqa: E501
            "bt_type": (str,),  # noqa: E501
            "column_name": (str,),  # noqa: E501
            "default_value": (btm_parameter1.BTMParameter1,),  # noqa: E501
            "icon_uri": (str,),  # noqa: E501
            "localizable_name": (str,),  # noqa: E501
            "localized_name": (str,),  # noqa: E501
            "parameter_id": (str,),  # noqa: E501
            "parameter_name": (str,),  # noqa: E501
            "strings_to_localize": ([str],),  # noqa: E501
            "ui_hint": (str,),  # noqa: E501
            "ui_hints": ([str],),  # noqa: E501
            "visibility_condition": (
                bt_parameter_visibility_condition177.BTParameterVisibilityCondition177,
            ),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return {
            "bt_type": {
                "BTParameterSpecAppearance-1740": bt_parameter_spec_appearance1740.BTParameterSpecAppearance1740,
                "BTParameterSpecForeignId-172": bt_parameter_spec_foreign_id172.BTParameterSpecForeignId172,
                "BTParameterSpecMaterial-2700": bt_parameter_spec_material2700.BTParameterSpecMaterial2700,
                "BTParameterSpecQuantity-173": bt_parameter_spec_quantity173.BTParameterSpecQuantity173,
                "BTParameterSpecNullableQuantity-715": bt_parameter_spec_nullable_quantity715.BTParameterSpecNullableQuantity715,
                "BTParameterSpecString-175": bt_parameter_spec_string175.BTParameterSpecString175,
                "BTParameterSpecReference-2789": bt_parameter_spec_reference2789.BTParameterSpecReference2789,
                "BTParameterSpecDatabase-1071": bt_parameter_spec_database1071.BTParameterSpecDatabase1071,
                "BTParameterSpecArray-2600": bt_parameter_spec_array2600.BTParameterSpecArray2600,
                "BTParameterSpecLookupTablePath-761": bt_parameter_spec_lookup_table_path761.BTParameterSpecLookupTablePath761,
                "BTParameterSpecBoolean-170": bt_parameter_spec_boolean170.BTParameterSpecBoolean170,
                "BTParameterSpecEnum-171": bt_parameter_spec_enum171.BTParameterSpecEnum171,
                "BTParameterSpecFeatureList-703": bt_parameter_spec_feature_list703.BTParameterSpecFeatureList703,
                "BTParameterSpecQuery-174": bt_parameter_spec_query174.BTParameterSpecQuery174,
                "BTParameterSpecDerived-736": bt_parameter_spec_derived736.BTParameterSpecDerived736,
            }
        }

    attribute_map = {
        "additional_localized_strings": "additionalLocalizedStrings",  # noqa: E501
        "bt_type": "btType",  # noqa: E501
        "column_name": "columnName",  # noqa: E501
        "default_value": "defaultValue",  # noqa: E501
        "icon_uri": "iconUri",  # noqa: E501
        "localizable_name": "localizableName",  # noqa: E501
        "localized_name": "localizedName",  # noqa: E501
        "parameter_id": "parameterId",  # noqa: E501
        "parameter_name": "parameterName",  # noqa: E501
        "strings_to_localize": "stringsToLocalize",  # noqa: E501
        "ui_hint": "uiHint",  # noqa: E501
        "ui_hints": "uiHints",  # noqa: E501
        "visibility_condition": "visibilityCondition",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_parameter_spec6.BTParameterSpec6 - a model defined in OpenAPI

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
            additional_localized_strings (int): [optional]  # noqa: E501
            bt_type (str): [optional]  # noqa: E501
            column_name (str): [optional]  # noqa: E501
            default_value (btm_parameter1.BTMParameter1): [optional]  # noqa: E501
            icon_uri (str): [optional]  # noqa: E501
            localizable_name (str): [optional]  # noqa: E501
            localized_name (str): [optional]  # noqa: E501
            parameter_id (str): [optional]  # noqa: E501
            parameter_name (str): [optional]  # noqa: E501
            strings_to_localize ([str]): [optional]  # noqa: E501
            ui_hint (str): [optional]  # noqa: E501
            ui_hints ([str]): [optional]  # noqa: E501
            visibility_condition (bt_parameter_visibility_condition177.BTParameterVisibilityCondition177): [optional]  # noqa: E501
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
