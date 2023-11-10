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

class AlignmentSource(object):
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
        'scenario_id': 'str',
        'probes': 'list[str]'
    }

    attribute_map = {
        'scenario_id': 'scenario_id',
        'probes': 'probes'
    }

    def __init__(self, scenario_id=None, probes=None):  # noqa: E501
        """AlignmentSource - a model defined in Swagger"""  # noqa: E501
        self._scenario_id = None
        self._probes = None
        self.discriminator = None
        self.scenario_id = scenario_id
        self.probes = probes

    @property
    def scenario_id(self):
        """Gets the scenario_id of this AlignmentSource.  # noqa: E501

        Unique ID for user session.  # noqa: E501

        :return: The scenario_id of this AlignmentSource.  # noqa: E501
        :rtype: str
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this AlignmentSource.

        Unique ID for user session.  # noqa: E501

        :param scenario_id: The scenario_id of this AlignmentSource.  # noqa: E501
        :type: str
        """
        if scenario_id is None:
            raise ValueError("Invalid value for `scenario_id`, must not be `None`")  # noqa: E501

        self._scenario_id = scenario_id

    @property
    def probes(self):
        """Gets the probes of this AlignmentSource.  # noqa: E501

        List of ID's of probes used to compute alignment.  # noqa: E501

        :return: The probes of this AlignmentSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        """Sets the probes of this AlignmentSource.

        List of ID's of probes used to compute alignment.  # noqa: E501

        :param probes: The probes of this AlignmentSource.  # noqa: E501
        :type: list[str]
        """
        if probes is None:
            raise ValueError("Invalid value for `probes`, must not be `None`")  # noqa: E501

        self._probes = probes

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
        if issubclass(AlignmentSource, dict):
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
        if not isinstance(other, AlignmentSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other