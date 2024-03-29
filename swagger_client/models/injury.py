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

class Injury(object):
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
        'name': 'InjuryTypeEnum',
        'location': 'InjuryLocationEnum',
        'severity': 'InjurySeverityEnum',
        'status': 'InjuryStatusEnum',
        'source_character': 'str'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'severity': 'severity',
        'status': 'status',
        'source_character': 'source_character'
    }

    def __init__(self, name=None, location=None, severity=None, status=None, source_character=None):  # noqa: E501
        """Injury - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._location = None
        self._severity = None
        self._status = None
        self._source_character = None
        self.discriminator = None
        self.name = name
        self.location = location
        if severity is not None:
            self.severity = severity
        self.status = status
        if source_character is not None:
            self.source_character = source_character

    @property
    def name(self):
        """Gets the name of this Injury.  # noqa: E501


        :return: The name of this Injury.  # noqa: E501
        :rtype: InjuryTypeEnum
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Injury.


        :param name: The name of this Injury.  # noqa: E501
        :type: InjuryTypeEnum
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def location(self):
        """Gets the location of this Injury.  # noqa: E501


        :return: The location of this Injury.  # noqa: E501
        :rtype: InjuryLocationEnum
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Injury.


        :param location: The location of this Injury.  # noqa: E501
        :type: InjuryLocationEnum
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def severity(self):
        """Gets the severity of this Injury.  # noqa: E501


        :return: The severity of this Injury.  # noqa: E501
        :rtype: InjurySeverityEnum
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Injury.


        :param severity: The severity of this Injury.  # noqa: E501
        :type: InjurySeverityEnum
        """

        self._severity = severity

    @property
    def status(self):
        """Gets the status of this Injury.  # noqa: E501


        :return: The status of this Injury.  # noqa: E501
        :rtype: InjuryStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Injury.


        :param status: The status of this Injury.  # noqa: E501
        :type: InjuryStatusEnum
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def source_character(self):
        """Gets the source_character of this Injury.  # noqa: E501

        The character id of the person responsible for the injury, subject to the character's `directness_of_causality`  # noqa: E501

        :return: The source_character of this Injury.  # noqa: E501
        :rtype: str
        """
        return self._source_character

    @source_character.setter
    def source_character(self, source_character):
        """Sets the source_character of this Injury.

        The character id of the person responsible for the injury, subject to the character's `directness_of_causality`  # noqa: E501

        :param source_character: The source_character of this Injury.  # noqa: E501
        :type: str
        """

        self._source_character = source_character

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
        if issubclass(Injury, dict):
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
        if not isinstance(other, Injury):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
