# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Supplies(object):
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
        'type': 'SupplyTypeEnum',
        'reusable': 'bool',
        'quantity': 'int'
    }

    attribute_map = {
        'type': 'type',
        'reusable': 'reusable',
        'quantity': 'quantity'
    }

    def __init__(self, type=None, reusable=False, quantity=None):  # noqa: E501
        """Supplies - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._reusable = None
        self._quantity = None
        self.discriminator = None
        self.type = type
        if reusable is not None:
            self.reusable = reusable
        self.quantity = quantity

    @property
    def type(self):
        """Gets the type of this Supplies.  # noqa: E501


        :return: The type of this Supplies.  # noqa: E501
        :rtype: SupplyTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Supplies.


        :param type: The type of this Supplies.  # noqa: E501
        :type: SupplyTypeEnum
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def reusable(self):
        """Gets the reusable of this Supplies.  # noqa: E501

        Whether or not item is consumable/reusable  # noqa: E501

        :return: The reusable of this Supplies.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this Supplies.

        Whether or not item is consumable/reusable  # noqa: E501

        :param reusable: The reusable of this Supplies.  # noqa: E501
        :type: bool
        """

        self._reusable = reusable

    @property
    def quantity(self):
        """Gets the quantity of this Supplies.  # noqa: E501

        Number of items available in the medical bag  # noqa: E501

        :return: The quantity of this Supplies.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Supplies.

        Number of items available in the medical bag  # noqa: E501

        :param quantity: The quantity of this Supplies.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

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
        if issubclass(Supplies, dict):
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
        if not isinstance(other, Supplies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
