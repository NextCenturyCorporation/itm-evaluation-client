# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Dry Run Evaluation.  The API is based on the OpenAPI 3.0.3 specification.  # noqa: E501

    OpenAPI spec version: 0.3.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MilitaryRankEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    E_1 = "E-1"
    E_2 = "E-2"
    E_3 = "E-3"
    E_4 = "E-4"
    E_5 = "E-5"
    E_6 = "E-6"
    E_7 = "E-7"
    E_8 = "E-8"
    E_9 = "E-9"
    E_9_SPECIAL_ = "E-9 (special)"
    W_1 = "W-1"
    W_2 = "W-2"
    W_3 = "W-3"
    W_4 = "W-4"
    W_5 = "W-5"
    O_1 = "O-1"
    O_2 = "O-2"
    O_3 = "O-3"
    O_4 = "O-4"
    O_5 = "O-5"
    O_6 = "O-6"
    O_7 = "O-7"
    O_8 = "O-8"
    O_9 = "O-9"
    O_10 = "O-10"
    SPECIAL = "Special"
    SPECIAL_NAVY_ = "Special (Navy)"
    SPECIAL_COAST_GUARD_ = "Special (Coast Guard)"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """MilitaryRankEnum - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(MilitaryRankEnum, dict):
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
        if not isinstance(other, MilitaryRankEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
