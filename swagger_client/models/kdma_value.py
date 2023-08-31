# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class KDMAValue(object):
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
        'kdma': 'str',
        'value': 'float'
    }

    attribute_map = {
        'kdma': 'kdma',
        'value': 'value'
    }

    def __init__(self, kdma=None, value=None):  # noqa: E501
        """KDMAValue - a model defined in Swagger"""  # noqa: E501
        self._kdma = None
        self._value = None
        self.discriminator = None
        self.kdma = kdma
        self.value = value

    @property
    def kdma(self):
        """Gets the kdma of this KDMAValue.  # noqa: E501

        KDMA name  # noqa: E501

        :return: The kdma of this KDMAValue.  # noqa: E501
        :rtype: str
        """
        return self._kdma

    @kdma.setter
    def kdma(self, kdma):
        """Sets the kdma of this KDMAValue.

        KDMA name  # noqa: E501

        :param kdma: The kdma of this KDMAValue.  # noqa: E501
        :type: str
        """
        if kdma is None:
            raise ValueError("Invalid value for `kdma`, must not be `None`")  # noqa: E501

        self._kdma = kdma

    @property
    def value(self):
        """Gets the value of this KDMAValue.  # noqa: E501

        target alignment value  # noqa: E501

        :return: The value of this KDMAValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this KDMAValue.

        target alignment value  # noqa: E501

        :param value: The value of this KDMAValue.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(KDMAValue, dict):
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
        if not isinstance(other, KDMAValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
