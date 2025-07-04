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
    from omni.importer.onshape.onshape_client.oas.models import bt_curve_geometry114
except ImportError:
    bt_curve_geometry114 = sys.modules["omni.importer.onshape.onshape_client.oas.models.bt_curve_geometry114"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btm_parameter1
except ImportError:
    btm_parameter1 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btm_parameter1"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btm_sketch_curve4
except ImportError:
    btm_sketch_curve4 = sys.modules["omni.importer.onshape.onshape_client.oas.models.btm_sketch_curve4"]
try:
    from omni.importer.onshape.onshape_client.oas.models import btm_sketch_curve_segment155_all_of
except ImportError:
    btm_sketch_curve_segment155_all_of = sys.modules[
        "omni.importer.onshape.onshape_client.oas.models.btm_sketch_curve_segment155_all_of"
    ]


class BTMSketchCurveSegment155(ModelComposed):
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
            "bt_type": (str,),  # noqa: E501
            "end_param": (float,),  # noqa: E501
            "end_point_id": (str,),  # noqa: E501
            "start_param": (float,),  # noqa: E501
            "start_point_id": (str,),  # noqa: E501
            "control_box_ids": ([str],),  # noqa: E501
            "entity_id": (str,),  # noqa: E501
            "entity_id_and_replace_in_dependent_fields": (str,),  # noqa: E501
            "import_microversion": (str,),  # noqa: E501
            "is_construction": (bool,),  # noqa: E501
            "namespace": (str,),  # noqa: E501
            "node_id": (str,),  # noqa: E501
            "parameters": ([btm_parameter1.BTMParameter1],),  # noqa: E501
            "center_id": (str,),  # noqa: E501
            "geometry": (bt_curve_geometry114.BTCurveGeometry114,),  # noqa: E501
            "internal_ids": ([str],),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        "bt_type": "btType",  # noqa: E501
        "end_param": "endParam",  # noqa: E501
        "end_point_id": "endPointId",  # noqa: E501
        "start_param": "startParam",  # noqa: E501
        "start_point_id": "startPointId",  # noqa: E501
        "control_box_ids": "controlBoxIds",  # noqa: E501
        "entity_id": "entityId",  # noqa: E501
        "entity_id_and_replace_in_dependent_fields": "entityIdAndReplaceInDependentFields",  # noqa: E501
        "import_microversion": "importMicroversion",  # noqa: E501
        "is_construction": "isConstruction",  # noqa: E501
        "namespace": "namespace",  # noqa: E501
        "node_id": "nodeId",  # noqa: E501
        "parameters": "parameters",  # noqa: E501
        "center_id": "centerId",  # noqa: E501
        "geometry": "geometry",  # noqa: E501
        "internal_ids": "internalIds",  # noqa: E501
    }

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_from_server",
            "_path_to_item",
            "_configuration",
            "_composed_instances",
            "_var_name_to_model_instances",
            "_additional_properties_model_instances",
        ]
    )

    def __init__(
        self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs
    ):  # noqa: E501
        """btm_sketch_curve_segment155.BTMSketchCurveSegment155 - a model defined in OpenAPI

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
            bt_type (str): [optional]  # noqa: E501
            end_param (float): [optional]  # noqa: E501
            end_point_id (str): [optional]  # noqa: E501
            start_param (float): [optional]  # noqa: E501
            start_point_id (str): [optional]  # noqa: E501
            control_box_ids ([str]): [optional]  # noqa: E501
            entity_id (str): [optional]  # noqa: E501
            entity_id_and_replace_in_dependent_fields (str): [optional]  # noqa: E501
            import_microversion (str): [optional]  # noqa: E501
            is_construction (bool): [optional]  # noqa: E501
            namespace (str): [optional]  # noqa: E501
            node_id (str): [optional]  # noqa: E501
            parameters ([btm_parameter1.BTMParameter1]): [optional]  # noqa: E501
            center_id (str): [optional]  # noqa: E501
            geometry (bt_curve_geometry114.BTCurveGeometry114): [optional]  # noqa: E501
            internal_ids ([str]): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        constant_args = {
            "_check_type": _check_type,
            "_path_to_item": _path_to_item,
            "_from_server": _from_server,
            "_configuration": _configuration,
        }
        required_args = {}
        # remove args whose value is Null because they are unset
        required_arg_names = list(required_args.keys())
        for required_arg_name in required_arg_names:
            if required_args[required_arg_name] is nulltype.Null:
                del required_args[required_arg_name]
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in six.iteritems(kwargs):
            if (
                var_name in unused_args
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and not self._additional_properties_model_instances
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @staticmethod
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
            "anyOf": [],
            "allOf": [
                btm_sketch_curve4.BTMSketchCurve4,
                btm_sketch_curve_segment155_all_of.BTMSketchCurveSegment155AllOf,
            ],
            "oneOf": [],
        }
