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
    from omni.importer.onshape.onshape_client.oas.models import bt_common_units_info
except ImportError:
    bt_common_units_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_common_units_info"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_default_units_info
except ImportError:
    bt_default_units_info = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_default_units_info"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_material_library_settings_info
except ImportError:
    bt_material_library_settings_info = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_material_library_settings_info"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_substitute_approver_info
except ImportError:
    bt_substitute_approver_info = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_substitute_approver_info"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_units_display_precision
except ImportError:
    bt_units_display_precision = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_units_display_precision"]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_units_maximum_display_precision_info
except ImportError:
    bt_units_maximum_display_precision_info = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_units_maximum_display_precision_info"
    ]
try:
    from omni.importer.onshape.onshape_client.oas.models import bt_view_manipulation_mouse_key_mapping_info
except ImportError:
    bt_view_manipulation_mouse_key_mapping_info = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.bt_view_manipulation_mouse_key_mapping_info"
    ]


class BTUserSettingsInfo(ModelNormal):
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
            "common_units": (bt_common_units_info.BTCommonUnitsInfo,),  # noqa: E501
            "custom_colors": ([str],),  # noqa: E501
            "default_units": (bt_default_units_info.BTDefaultUnitsInfo,),  # noqa: E501
            "drawing_background_id": (int,),  # noqa: E501
            "enforce_application_acl": (bool,),  # noqa: E501
            "export_drawing_options": (str,),  # noqa: E501
            "export_solid_options": (str,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "import_options": (str,),  # noqa: E501
            "locale": (str,),  # noqa: E501
            "material_library_settings": (
                bt_material_library_settings_info.BTMaterialLibrarySettingsInfo,
            ),  # noqa: E501
            "mini_toolbar_settings": (str,),  # noqa: E501
            "mouse_actions": (str,),  # noqa: E501
            "reverse_scroll_wheel_zoom_direction": (bool,),  # noqa: E501
            "startup_page": (int,),  # noqa: E501
            "substitute_approvers": ([bt_substitute_approver_info.BTSubstituteApproverInfo],),  # noqa: E501
            "units_display_precision": (bt_units_display_precision.BTUnitsDisplayPrecision,),  # noqa: E501
            "units_maximum_display_precision": (
                bt_units_maximum_display_precision_info.BTUnitsMaximumDisplayPrecisionInfo,
            ),  # noqa: E501
            "use24_hour_time": (bool,),  # noqa: E501
            "view_manipulation_mouse_key_mapping": (
                bt_view_manipulation_mouse_key_mapping_info.BTViewManipulationMouseKeyMappingInfo,
            ),  # noqa: E501
            "view_mapping_id": (int,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "common_units": "commonUnits",  # noqa: E501
        "custom_colors": "customColors",  # noqa: E501
        "default_units": "defaultUnits",  # noqa: E501
        "drawing_background_id": "drawingBackgroundId",  # noqa: E501
        "enforce_application_acl": "enforceApplicationAcl",  # noqa: E501
        "export_drawing_options": "exportDrawingOptions",  # noqa: E501
        "export_solid_options": "exportSolidOptions",  # noqa: E501
        "id": "id",  # noqa: E501
        "import_options": "importOptions",  # noqa: E501
        "locale": "locale",  # noqa: E501
        "material_library_settings": "materialLibrarySettings",  # noqa: E501
        "mini_toolbar_settings": "miniToolbarSettings",  # noqa: E501
        "mouse_actions": "mouseActions",  # noqa: E501
        "reverse_scroll_wheel_zoom_direction": "reverseScrollWheelZoomDirection",  # noqa: E501
        "startup_page": "startupPage",  # noqa: E501
        "substitute_approvers": "substituteApprovers",  # noqa: E501
        "units_display_precision": "unitsDisplayPrecision",  # noqa: E501
        "units_maximum_display_precision": "unitsMaximumDisplayPrecision",  # noqa: E501
        "use24_hour_time": "use24HourTime",  # noqa: E501
        "view_manipulation_mouse_key_mapping": "viewManipulationMouseKeyMapping",  # noqa: E501
        "view_mapping_id": "viewMappingId",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_user_settings_info.BTUserSettingsInfo - a model defined in OpenAPI

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
            common_units (bt_common_units_info.BTCommonUnitsInfo): [optional]  # noqa: E501
            custom_colors ([str]): [optional]  # noqa: E501
            default_units (bt_default_units_info.BTDefaultUnitsInfo): [optional]  # noqa: E501
            drawing_background_id (int): [optional]  # noqa: E501
            enforce_application_acl (bool): [optional]  # noqa: E501
            export_drawing_options (str): [optional]  # noqa: E501
            export_solid_options (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            import_options (str): [optional]  # noqa: E501
            locale (str): [optional]  # noqa: E501
            material_library_settings (bt_material_library_settings_info.BTMaterialLibrarySettingsInfo): [optional]  # noqa: E501
            mini_toolbar_settings (str): [optional]  # noqa: E501
            mouse_actions (str): [optional]  # noqa: E501
            reverse_scroll_wheel_zoom_direction (bool): [optional]  # noqa: E501
            startup_page (int): [optional]  # noqa: E501
            substitute_approvers ([bt_substitute_approver_info.BTSubstituteApproverInfo]): [optional]  # noqa: E501
            units_display_precision (bt_units_display_precision.BTUnitsDisplayPrecision): [optional]  # noqa: E501
            units_maximum_display_precision (bt_units_maximum_display_precision_info.BTUnitsMaximumDisplayPrecisionInfo): [optional]  # noqa: E501
            use24_hour_time (bool): [optional]  # noqa: E501
            view_manipulation_mouse_key_mapping (bt_view_manipulation_mouse_key_mapping_info.BTViewManipulationMouseKeyMappingInfo): [optional]  # noqa: E501
            view_mapping_id (int): [optional]  # noqa: E501
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
