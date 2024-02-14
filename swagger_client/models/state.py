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

class State(object):
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
        'unstructured': 'str',
        'elapsed_time': 'int',
        'scenario_complete': 'bool',
        'mission': 'Mission',
        'environment': 'Environment',
        'threat_state': 'ThreatState',
        'supplies': 'list[Supplies]',
        'characters': 'list[Character]'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'elapsed_time': 'elapsed_time',
        'scenario_complete': 'scenario_complete',
        'mission': 'mission',
        'environment': 'environment',
        'threat_state': 'threat_state',
        'supplies': 'supplies',
        'characters': 'characters'
    }

    def __init__(self, unstructured=None, elapsed_time=None, scenario_complete=None, mission=None, environment=None, threat_state=None, supplies=None, characters=None):  # noqa: E501
        """State - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._elapsed_time = None
        self._scenario_complete = None
        self._mission = None
        self._environment = None
        self._threat_state = None
        self._supplies = None
        self._characters = None
        self.discriminator = None
        self.unstructured = unstructured
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if scenario_complete is not None:
            self.scenario_complete = scenario_complete
        if mission is not None:
            self.mission = mission
        self.environment = environment
        if threat_state is not None:
            self.threat_state = threat_state
        self.supplies = supplies
        self.characters = characters

    @property
    def unstructured(self):
        """Gets the unstructured of this State.  # noqa: E501

        Natural language, plain text description of a scene's state  # noqa: E501

        :return: The unstructured of this State.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this State.

        Natural language, plain text description of a scene's state  # noqa: E501

        :param unstructured: The unstructured of this State.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this State.  # noqa: E501

        the simulated elapsed time (in seconds) since the scenario started  # noqa: E501

        :return: The elapsed_time of this State.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this State.

        the simulated elapsed time (in seconds) since the scenario started  # noqa: E501

        :param elapsed_time: The elapsed_time of this State.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def scenario_complete(self):
        """Gets the scenario_complete of this State.  # noqa: E501

        set to true if the scenario is complete; subsequent calls involving that scenario will return an error code  # noqa: E501

        :return: The scenario_complete of this State.  # noqa: E501
        :rtype: bool
        """
        return self._scenario_complete

    @scenario_complete.setter
    def scenario_complete(self, scenario_complete):
        """Sets the scenario_complete of this State.

        set to true if the scenario is complete; subsequent calls involving that scenario will return an error code  # noqa: E501

        :param scenario_complete: The scenario_complete of this State.  # noqa: E501
        :type: bool
        """

        self._scenario_complete = scenario_complete

    @property
    def mission(self):
        """Gets the mission of this State.  # noqa: E501


        :return: The mission of this State.  # noqa: E501
        :rtype: Mission
        """
        return self._mission

    @mission.setter
    def mission(self, mission):
        """Sets the mission of this State.


        :param mission: The mission of this State.  # noqa: E501
        :type: Mission
        """

        self._mission = mission

    @property
    def environment(self):
        """Gets the environment of this State.  # noqa: E501


        :return: The environment of this State.  # noqa: E501
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this State.


        :param environment: The environment of this State.  # noqa: E501
        :type: Environment
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def threat_state(self):
        """Gets the threat_state of this State.  # noqa: E501


        :return: The threat_state of this State.  # noqa: E501
        :rtype: ThreatState
        """
        return self._threat_state

    @threat_state.setter
    def threat_state(self, threat_state):
        """Sets the threat_state of this State.


        :param threat_state: The threat_state of this State.  # noqa: E501
        :type: ThreatState
        """

        self._threat_state = threat_state

    @property
    def supplies(self):
        """Gets the supplies of this State.  # noqa: E501

        A list of supplies available to the medic  # noqa: E501

        :return: The supplies of this State.  # noqa: E501
        :rtype: list[Supplies]
        """
        return self._supplies

    @supplies.setter
    def supplies(self, supplies):
        """Sets the supplies of this State.

        A list of supplies available to the medic  # noqa: E501

        :param supplies: The supplies of this State.  # noqa: E501
        :type: list[Supplies]
        """
        if supplies is None:
            raise ValueError("Invalid value for `supplies`, must not be `None`")  # noqa: E501

        self._supplies = supplies

    @property
    def characters(self):
        """Gets the characters of this State.  # noqa: E501

        A list of characters in the scene, including injured patients, civilians, medics, etc.  # noqa: E501

        :return: The characters of this State.  # noqa: E501
        :rtype: list[Character]
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        """Sets the characters of this State.

        A list of characters in the scene, including injured patients, civilians, medics, etc.  # noqa: E501

        :param characters: The characters of this State.  # noqa: E501
        :type: list[Character]
        """
        if characters is None:
            raise ValueError("Invalid value for `characters`, must not be `None`")  # noqa: E501

        self._characters = characters

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
        if issubclass(State, dict):
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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
