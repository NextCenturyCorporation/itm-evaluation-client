# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.  # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProbeConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'probe_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'probe_id': 'probe_id',
        'description': 'description'
    }

    def __init__(self, probe_id=None, description=None):  # noqa: E501
        """ProbeConfig - a model defined in Swagger"""  # noqa: E501
        self._probe_id = None
        self._description = None
        self.discriminator = None
        if probe_id is not None:
            self.probe_id = probe_id
        if description is not None:
            self.description = description

    @property
    def probe_id(self):
        """Gets the probe_id of this ProbeConfig.  # noqa: E501

        A valid probe_id from the appropriate TA1  # noqa: E501

        :return: The probe_id of this ProbeConfig.  # noqa: E501
        :rtype: str
        """
        return self._probe_id

    @probe_id.setter
    def probe_id(self, probe_id):
        """Sets the probe_id of this ProbeConfig.

        A valid probe_id from the appropriate TA1  # noqa: E501

        :param probe_id: The probe_id of this ProbeConfig.  # noqa: E501
        :type: str
        """

        self._probe_id = probe_id

    @property
    def description(self):
        """Gets the description of this ProbeConfig.  # noqa: E501

        A description of the probe for use by TA1  # noqa: E501

        :return: The description of this ProbeConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProbeConfig.

        A description of the probe for use by TA1  # noqa: E501

        :param description: The description of this ProbeConfig.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProbeConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProbeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
