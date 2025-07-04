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
    from omni.importer.onshape.onshape_client.oas.models import bt_element_location_params
except ImportError:
    bt_element_location_params = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_element_location_params"]


class BTDrawingParams(ModelNormal):
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
        ("hidden_lines",): {"DRAFTING": "DRAFTING", "EXCLUDED": "EXCLUDED", "MARKED": "MARKED"},
        ("reference_type_enum",): {
            "UNKNOWN": "UNKNOWN",
            "PARTSTUDIO": "PARTSTUDIO",
            "ASSEMBLY": "ASSEMBLY",
            "PART": "PART",
            "FLATTENED_PART": "FLATTENED_PART",
            "COMPOSITE_PART": "COMPOSITE_PART",
            "MESH_PART": "MESH_PART",
            "SURFACE": "SURFACE",
            "SKETCH": "SKETCH",
            "CURVE": "CURVE",
        },
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
            "border": (bool,),  # noqa: E501
            "compute_intersection": (bool,),  # noqa: E501
            "decimal_separator": (str,),  # noqa: E501
            "document_id": (str,),  # noqa: E501
            "document_microversion_id": (str,),  # noqa: E501
            "drawing_name": (str,),  # noqa: E501
            "element_configuration": (str,),  # noqa: E501
            "element_id": (str,),  # noqa: E501
            "element_microversion_id": (str,),  # noqa: E501
            "external_document_id": (str,),  # noqa: E501
            "external_document_version_id": (str,),  # noqa: E501
            "hidden_lines": (str,),  # noqa: E501
            "include_surfaces": (bool,),  # noqa: E501
            "is_flattened_part": (bool,),  # noqa: E501
            "is_sketch_only": (bool,),  # noqa: E501
            "is_surface": (bool,),  # noqa: E501
            "language": (str,),  # noqa: E501
            "location": (bt_element_location_params.BTElementLocationParams,),  # noqa: E501
            "model_type": (str,),  # noqa: E501
            "number_horizontal_zones": (int,),  # noqa: E501
            "number_vertical_zones": (int,),  # noqa: E501
            "part_id": (str,),  # noqa: E501
            "part_number": (str,),  # noqa: E501
            "part_query": (str,),  # noqa: E501
            "projection": (str,),  # noqa: E501
            "pure_sketch": (bool,),  # noqa: E501
            "quality_option": (str,),  # noqa: E501
            "reference_type": (int,),  # noqa: E501
            "reference_type_enum": (str,),  # noqa: E501
            "revision": (str,),  # noqa: E501
            "show_cut_geom_only": (bool,),  # noqa: E501
            "simplification_option": (str,),  # noqa: E501
            "simplification_threshold": (float,),  # noqa: E501
            "size": (str,),  # noqa: E501
            "sketch_ids": ([str],),  # noqa: E501
            "standard": (str,),  # noqa: E501
            "start_zones": (str,),  # noqa: E501
            "template_args": ([str],),  # noqa: E501
            "template_document_id": (str,),  # noqa: E501
            "template_element_id": (str,),  # noqa: E501
            "template_name": (str,),  # noqa: E501
            "template_version_id": (str,),  # noqa: E501
            "template_workspace_id": (str,),  # noqa: E501
            "titleblock": (bool,),  # noqa: E501
            "units": (str,),  # noqa: E501
            "views": (str,),  # noqa: E501
            "workspace_id": (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "border": "border",  # noqa: E501
        "compute_intersection": "computeIntersection",  # noqa: E501
        "decimal_separator": "decimalSeparator",  # noqa: E501
        "document_id": "documentId",  # noqa: E501
        "document_microversion_id": "documentMicroversionId",  # noqa: E501
        "drawing_name": "drawingName",  # noqa: E501
        "element_configuration": "elementConfiguration",  # noqa: E501
        "element_id": "elementId",  # noqa: E501
        "element_microversion_id": "elementMicroversionId",  # noqa: E501
        "external_document_id": "externalDocumentId",  # noqa: E501
        "external_document_version_id": "externalDocumentVersionId",  # noqa: E501
        "hidden_lines": "hiddenLines",  # noqa: E501
        "include_surfaces": "includeSurfaces",  # noqa: E501
        "is_flattened_part": "isFlattenedPart",  # noqa: E501
        "is_sketch_only": "isSketchOnly",  # noqa: E501
        "is_surface": "isSurface",  # noqa: E501
        "language": "language",  # noqa: E501
        "location": "location",  # noqa: E501
        "model_type": "modelType",  # noqa: E501
        "number_horizontal_zones": "numberHorizontalZones",  # noqa: E501
        "number_vertical_zones": "numberVerticalZones",  # noqa: E501
        "part_id": "partId",  # noqa: E501
        "part_number": "partNumber",  # noqa: E501
        "part_query": "partQuery",  # noqa: E501
        "projection": "projection",  # noqa: E501
        "pure_sketch": "pureSketch",  # noqa: E501
        "quality_option": "qualityOption",  # noqa: E501
        "reference_type": "referenceType",  # noqa: E501
        "reference_type_enum": "referenceTypeEnum",  # noqa: E501
        "revision": "revision",  # noqa: E501
        "show_cut_geom_only": "showCutGeomOnly",  # noqa: E501
        "simplification_option": "simplificationOption",  # noqa: E501
        "simplification_threshold": "simplificationThreshold",  # noqa: E501
        "size": "size",  # noqa: E501
        "sketch_ids": "sketchIds",  # noqa: E501
        "standard": "standard",  # noqa: E501
        "start_zones": "startZones",  # noqa: E501
        "template_args": "templateArgs",  # noqa: E501
        "template_document_id": "templateDocumentId",  # noqa: E501
        "template_element_id": "templateElementId",  # noqa: E501
        "template_name": "templateName",  # noqa: E501
        "template_version_id": "templateVersionId",  # noqa: E501
        "template_workspace_id": "templateWorkspaceId",  # noqa: E501
        "titleblock": "titleblock",  # noqa: E501
        "units": "units",  # noqa: E501
        "views": "views",  # noqa: E501
        "workspace_id": "workspaceId",  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set(["_data_store", "_check_type", "_from_server", "_path_to_item", "_configuration"])

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """bt_drawing_params.BTDrawingParams - a model defined in OpenAPI

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
            border (bool): [optional]  # noqa: E501
            compute_intersection (bool): [optional]  # noqa: E501
            decimal_separator (str): [optional]  # noqa: E501
            document_id (str): [optional]  # noqa: E501
            document_microversion_id (str): [optional]  # noqa: E501
            drawing_name (str): [optional]  # noqa: E501
            element_configuration (str): [optional]  # noqa: E501
            element_id (str): [optional]  # noqa: E501
            element_microversion_id (str): [optional]  # noqa: E501
            external_document_id (str): [optional]  # noqa: E501
            external_document_version_id (str): [optional]  # noqa: E501
            hidden_lines (str): [optional]  # noqa: E501
            include_surfaces (bool): [optional]  # noqa: E501
            is_flattened_part (bool): [optional]  # noqa: E501
            is_sketch_only (bool): [optional]  # noqa: E501
            is_surface (bool): [optional]  # noqa: E501
            language (str): [optional]  # noqa: E501
            location (bt_element_location_params.BTElementLocationParams): [optional]  # noqa: E501
            model_type (str): [optional]  # noqa: E501
            number_horizontal_zones (int): [optional]  # noqa: E501
            number_vertical_zones (int): [optional]  # noqa: E501
            part_id (str): [optional]  # noqa: E501
            part_number (str): [optional]  # noqa: E501
            part_query (str): [optional]  # noqa: E501
            projection (str): [optional]  # noqa: E501
            pure_sketch (bool): [optional]  # noqa: E501
            quality_option (str): [optional]  # noqa: E501
            reference_type (int): [optional]  # noqa: E501
            reference_type_enum (str): [optional]  # noqa: E501
            revision (str): [optional]  # noqa: E501
            show_cut_geom_only (bool): [optional]  # noqa: E501
            simplification_option (str): [optional]  # noqa: E501
            simplification_threshold (float): [optional]  # noqa: E501
            size (str): [optional]  # noqa: E501
            sketch_ids ([str]): [optional]  # noqa: E501
            standard (str): [optional]  # noqa: E501
            start_zones (str): [optional]  # noqa: E501
            template_args ([str]): [optional]  # noqa: E501
            template_document_id (str): [optional]  # noqa: E501
            template_element_id (str): [optional]  # noqa: E501
            template_name (str): [optional]  # noqa: E501
            template_version_id (str): [optional]  # noqa: E501
            template_workspace_id (str): [optional]  # noqa: E501
            titleblock (bool): [optional]  # noqa: E501
            units (str): [optional]  # noqa: E501
            views (str): [optional]  # noqa: E501
            workspace_id (str): [optional]  # noqa: E501
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
