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

class Conditions(object):
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
        'elapsed_time_lt': 'int',
        'elapsed_time_gt': 'int',
        'actions': 'list[list[str]]',
        'probes': 'list[str]',
        'probe_responses': 'list[str]',
        'character_vitals': 'list[ConditionsCharacterVitals]',
        'supplies': 'list[Supplies]'
    }

    attribute_map = {
        'elapsed_time_lt': 'elapsed_time_lt',
        'elapsed_time_gt': 'elapsed_time_gt',
        'actions': 'actions',
        'probes': 'probes',
        'probe_responses': 'probe_responses',
        'character_vitals': 'character_vitals',
        'supplies': 'supplies'
    }

    def __init__(self, elapsed_time_lt=None, elapsed_time_gt=None, actions=None, probes=None, probe_responses=None, character_vitals=None, supplies=None):  # noqa: E501
        """Conditions - a model defined in Swagger"""  # noqa: E501
        self._elapsed_time_lt = None
        self._elapsed_time_gt = None
        self._actions = None
        self._probes = None
        self._probe_responses = None
        self._character_vitals = None
        self._supplies = None
        self.discriminator = None
        if elapsed_time_lt is not None:
            self.elapsed_time_lt = elapsed_time_lt
        if elapsed_time_gt is not None:
            self.elapsed_time_gt = elapsed_time_gt
        if actions is not None:
            self.actions = actions
        if probes is not None:
            self.probes = probes
        if probe_responses is not None:
            self.probe_responses = probe_responses
        if character_vitals is not None:
            self.character_vitals = character_vitals
        if supplies is not None:
            self.supplies = supplies

    @property
    def elapsed_time_lt(self):
        """Gets the elapsed_time_lt of this Conditions.  # noqa: E501

        True if the scenario elapsed time (in seconds) is less than the specified value  # noqa: E501

        :return: The elapsed_time_lt of this Conditions.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time_lt

    @elapsed_time_lt.setter
    def elapsed_time_lt(self, elapsed_time_lt):
        """Sets the elapsed_time_lt of this Conditions.

        True if the scenario elapsed time (in seconds) is less than the specified value  # noqa: E501

        :param elapsed_time_lt: The elapsed_time_lt of this Conditions.  # noqa: E501
        :type: int
        """

        self._elapsed_time_lt = elapsed_time_lt

    @property
    def elapsed_time_gt(self):
        """Gets the elapsed_time_gt of this Conditions.  # noqa: E501

        True if the scenario elapsed time (in seconds) is greater than the specified value  # noqa: E501

        :return: The elapsed_time_gt of this Conditions.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time_gt

    @elapsed_time_gt.setter
    def elapsed_time_gt(self, elapsed_time_gt):
        """Sets the elapsed_time_gt of this Conditions.

        True if the scenario elapsed time (in seconds) is greater than the specified value  # noqa: E501

        :param elapsed_time_gt: The elapsed_time_gt of this Conditions.  # noqa: E501
        :type: int
        """

        self._elapsed_time_gt = elapsed_time_gt

    @property
    def actions(self):
        """Gets the actions of this Conditions.  # noqa: E501

        True if any of the specified lists of actions have been taken; multiple action ID lists have \"or\" semantics; multiple action IDs within a list have \"and\" semantics  # noqa: E501

        :return: The actions of this Conditions.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Conditions.

        True if any of the specified lists of actions have been taken; multiple action ID lists have \"or\" semantics; multiple action IDs within a list have \"and\" semantics  # noqa: E501

        :param actions: The actions of this Conditions.  # noqa: E501
        :type: list[list[str]]
        """

        self._actions = actions

    @property
    def probes(self):
        """Gets the probes of this Conditions.  # noqa: E501

        True if the specified list of probe_ids have been answered  # noqa: E501

        :return: The probes of this Conditions.  # noqa: E501
        :rtype: list[str]
        """
        return self._probes

    @probes.setter
    def probes(self, probes):
        """Sets the probes of this Conditions.

        True if the specified list of probe_ids have been answered  # noqa: E501

        :param probes: The probes of this Conditions.  # noqa: E501
        :type: list[str]
        """

        self._probes = probes

    @property
    def probe_responses(self):
        """Gets the probe_responses of this Conditions.  # noqa: E501

        True if the specified list of probe responses (choice) have been sent  # noqa: E501

        :return: The probe_responses of this Conditions.  # noqa: E501
        :rtype: list[str]
        """
        return self._probe_responses

    @probe_responses.setter
    def probe_responses(self, probe_responses):
        """Sets the probe_responses of this Conditions.

        True if the specified list of probe responses (choice) have been sent  # noqa: E501

        :param probe_responses: The probe_responses of this Conditions.  # noqa: E501
        :type: list[str]
        """

        self._probe_responses = probe_responses

    @property
    def character_vitals(self):
        """Gets the character_vitals of this Conditions.  # noqa: E501

        True if the any of the specified collection of vital values have been met for the specified character_id  # noqa: E501

        :return: The character_vitals of this Conditions.  # noqa: E501
        :rtype: list[ConditionsCharacterVitals]
        """
        return self._character_vitals

    @character_vitals.setter
    def character_vitals(self, character_vitals):
        """Sets the character_vitals of this Conditions.

        True if the any of the specified collection of vital values have been met for the specified character_id  # noqa: E501

        :param character_vitals: The character_vitals of this Conditions.  # noqa: E501
        :type: list[ConditionsCharacterVitals]
        """

        self._character_vitals = character_vitals

    @property
    def supplies(self):
        """Gets the supplies of this Conditions.  # noqa: E501

        True if any of the specified supplies reach or go below the specified quantity  # noqa: E501

        :return: The supplies of this Conditions.  # noqa: E501
        :rtype: list[Supplies]
        """
        return self._supplies

    @supplies.setter
    def supplies(self, supplies):
        """Sets the supplies of this Conditions.

        True if any of the specified supplies reach or go below the specified quantity  # noqa: E501

        :param supplies: The supplies of this Conditions.  # noqa: E501
        :type: list[Supplies]
        """

        self._supplies = supplies

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
        if issubclass(Conditions, dict):
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
        if not isinstance(other, Conditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
