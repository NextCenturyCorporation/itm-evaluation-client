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

class Scenario(object):
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
        'name': 'str',
        'first_scene': 'str',
        'session_complete': 'bool',
        'state': 'State',
        'scenes': 'list[Scene]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'first_scene': 'first_scene',
        'session_complete': 'session_complete',
        'state': 'state',
        'scenes': 'scenes'
    }

    def __init__(self, id=None, name=None, first_scene=None, session_complete=None, state=None, scenes=None):  # noqa: E501
        """Scenario - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._first_scene = None
        self._session_complete = None
        self._state = None
        self._scenes = None
        self.discriminator = None
        self.id = id
        self.name = name
        if first_scene is not None:
            self.first_scene = first_scene
        if session_complete is not None:
            self.session_complete = session_complete
        if state is not None:
            self.state = state
        if scenes is not None:
            self.scenes = scenes

    @property
    def id(self):
        """Gets the id of this Scenario.  # noqa: E501

        a globally unique id for the scenario  # noqa: E501

        :return: The id of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scenario.

        a globally unique id for the scenario  # noqa: E501

        :param id: The id of this Scenario.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Scenario.  # noqa: E501

        human-readable scenario name, not necessarily unique  # noqa: E501

        :return: The name of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Scenario.

        human-readable scenario name, not necessarily unique  # noqa: E501

        :param name: The name of this Scenario.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def first_scene(self):
        """Gets the first_scene of this Scenario.  # noqa: E501

        indicates the first/opening scene ID in the scenario  # noqa: E501

        :return: The first_scene of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._first_scene

    @first_scene.setter
    def first_scene(self, first_scene):
        """Sets the first_scene of this Scenario.

        indicates the first/opening scene ID in the scenario  # noqa: E501

        :param first_scene: The first_scene of this Scenario.  # noqa: E501
        :type: str
        """

        self._first_scene = first_scene

    @property
    def session_complete(self):
        """Gets the session_complete of this Scenario.  # noqa: E501

        set to true if the session is complete; that is, there are no more scenarios  # noqa: E501

        :return: The session_complete of this Scenario.  # noqa: E501
        :rtype: bool
        """
        return self._session_complete

    @session_complete.setter
    def session_complete(self, session_complete):
        """Sets the session_complete of this Scenario.

        set to true if the session is complete; that is, there are no more scenarios  # noqa: E501

        :param session_complete: The session_complete of this Scenario.  # noqa: E501
        :type: bool
        """

        self._session_complete = session_complete

    @property
    def state(self):
        """Gets the state of this Scenario.  # noqa: E501


        :return: The state of this Scenario.  # noqa: E501
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Scenario.


        :param state: The state of this Scenario.  # noqa: E501
        :type: State
        """

        self._state = state

    @property
    def scenes(self):
        """Gets the scenes of this Scenario.  # noqa: E501

        A list of specification for all scenes in the scenario  # noqa: E501

        :return: The scenes of this Scenario.  # noqa: E501
        :rtype: list[Scene]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        """Sets the scenes of this Scenario.

        A list of specification for all scenes in the scenario  # noqa: E501

        :param scenes: The scenes of this Scenario.  # noqa: E501
        :type: list[Scene]
        """

        self._scenes = scenes

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
        if issubclass(Scenario, dict):
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
        if not isinstance(other, Scenario):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
