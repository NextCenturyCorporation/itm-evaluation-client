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

class AidDelay(object):
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
        'id': 'str',
        'delay': 'float',
        'type': 'AidTypeEnum',
        'max_transport': 'int'
    }

    attribute_map = {
        'id': 'id',
        'delay': 'delay',
        'type': 'type',
        'max_transport': 'max_transport'
    }

    def __init__(self, id=None, delay=None, type=None, max_transport=None):  # noqa: E501
        """AidDelay - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._delay = None
        self._type = None
        self._max_transport = None
        self.discriminator = None
        self.id = id
        self.delay = delay
        if type is not None:
            self.type = type
        if max_transport is not None:
            self.max_transport = max_transport

    @property
    def id(self):
        """Gets the id of this AidDelay.  # noqa: E501

        An identifier for the evacuation opportunity, unique within the scene  # noqa: E501

        :return: The id of this AidDelay.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AidDelay.

        An identifier for the evacuation opportunity, unique within the scene  # noqa: E501

        :param id: The id of this AidDelay.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def delay(self):
        """Gets the delay of this AidDelay.  # noqa: E501

        CASEVAC or MEDEVAC timer, in minutes  # noqa: E501

        :return: The delay of this AidDelay.  # noqa: E501
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this AidDelay.

        CASEVAC or MEDEVAC timer, in minutes  # noqa: E501

        :param delay: The delay of this AidDelay.  # noqa: E501
        :type: float
        """
        if delay is None:
            raise ValueError("Invalid value for `delay`, must not be `None`")  # noqa: E501

        self._delay = delay

    @property
    def type(self):
        """Gets the type of this AidDelay.  # noqa: E501


        :return: The type of this AidDelay.  # noqa: E501
        :rtype: AidTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AidDelay.


        :param type: The type of this AidDelay.  # noqa: E501
        :type: AidTypeEnum
        """

        self._type = type

    @property
    def max_transport(self):
        """Gets the max_transport of this AidDelay.  # noqa: E501

        Maximum number of casualties that can be transported  # noqa: E501

        :return: The max_transport of this AidDelay.  # noqa: E501
        :rtype: int
        """
        return self._max_transport

    @max_transport.setter
    def max_transport(self, max_transport):
        """Sets the max_transport of this AidDelay.

        Maximum number of casualties that can be transported  # noqa: E501

        :param max_transport: The max_transport of this AidDelay.  # noqa: E501
        :type: int
        """

        self._max_transport = max_transport

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
        if issubclass(AidDelay, dict):
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
        if not isinstance(other, AidDelay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
