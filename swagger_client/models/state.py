# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the September milestone.  The API is based on the OpenAPI 3.0 specification.  # noqa: E501

    OpenAPI spec version: 0.2.0
    
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
        'elapsed_time': 'float',
        'scenario_complete': 'bool',
        'mission': 'Mission',
        'environment': 'Environment',
        'threat_state': 'ThreatState',
        'supplies': 'list[Supplies]',
        'casualties': 'list[Casualty]'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'elapsed_time': 'elapsedTime',
        'scenario_complete': 'scenario_complete',
        'mission': 'mission',
        'environment': 'environment',
        'threat_state': 'threat_state',
        'supplies': 'supplies',
        'casualties': 'casualties'
    }

    def __init__(self, unstructured=None, elapsed_time=None, scenario_complete=None, mission=None, environment=None, threat_state=None, supplies=None, casualties=None):  # noqa: E501
        """State - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._elapsed_time = None
        self._scenario_complete = None
        self._mission = None
        self._environment = None
        self._threat_state = None
        self._supplies = None
        self._casualties = None
        self.discriminator = None
        self.unstructured = unstructured
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if scenario_complete is not None:
            self.scenario_complete = scenario_complete
        if mission is not None:
            self.mission = mission
        if environment is not None:
            self.environment = environment
        if threat_state is not None:
            self.threat_state = threat_state
        if supplies is not None:
            self.supplies = supplies
        if casualties is not None:
            self.casualties = casualties

    @property
    def unstructured(self):
        """Gets the unstructured of this State.  # noqa: E501

        text description of current state  # noqa: E501

        :return: The unstructured of this State.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this State.

        text description of current state  # noqa: E501

        :param unstructured: The unstructured of this State.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this State.  # noqa: E501

        the elapsed time (in minutes) since the scenario started  # noqa: E501

        :return: The elapsed_time of this State.  # noqa: E501
        :rtype: float
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this State.

        the elapsed time (in minutes) since the scenario started  # noqa: E501

        :param elapsed_time: The elapsed_time of this State.  # noqa: E501
        :type: float
        """

        self._elapsed_time = elapsed_time

    @property
    def scenario_complete(self):
        """Gets the scenario_complete of this State.  # noqa: E501

        set to true if the scenario is complete; subsequent calls to /scenario/probe will return an error code  # noqa: E501

        :return: The scenario_complete of this State.  # noqa: E501
        :rtype: bool
        """
        return self._scenario_complete

    @scenario_complete.setter
    def scenario_complete(self, scenario_complete):
        """Sets the scenario_complete of this State.

        set to true if the scenario is complete; subsequent calls to /scenario/probe will return an error code  # noqa: E501

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

        a list of medical supplies available to the DM  # noqa: E501

        :return: The supplies of this State.  # noqa: E501
        :rtype: list[Supplies]
        """
        return self._supplies

    @supplies.setter
    def supplies(self, supplies):
        """Sets the supplies of this State.

        a list of medical supplies available to the DM  # noqa: E501

        :param supplies: The supplies of this State.  # noqa: E501
        :type: list[Supplies]
        """

        self._supplies = supplies

    @property
    def casualties(self):
        """Gets the casualties of this State.  # noqa: E501

        the list of casualties/patients in the scenario  # noqa: E501

        :return: The casualties of this State.  # noqa: E501
        :rtype: list[Casualty]
        """
        return self._casualties

    @casualties.setter
    def casualties(self, casualties):
        """Sets the casualties of this State.

        the list of casualties/patients in the scenario  # noqa: E501

        :param casualties: The casualties of this State.  # noqa: E501
        :type: list[Casualty]
        """

        self._casualties = casualties

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
