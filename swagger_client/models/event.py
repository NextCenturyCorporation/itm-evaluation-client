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

class Event(object):
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
        'type': 'EventTypeEnum',
        'source': 'str',
        'object': 'str',
        'when': 'float',
        'action_id': 'str',
        'relevant_state': 'list[str]'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'type': 'type',
        'source': 'source',
        'object': 'object',
        'when': 'when',
        'action_id': 'action_id',
        'relevant_state': 'relevant_state'
    }

    def __init__(self, unstructured=None, type=None, source=None, object=None, when=None, action_id=None, relevant_state=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._type = None
        self._source = None
        self._object = None
        self._when = None
        self._action_id = None
        self._relevant_state = None
        self.discriminator = None
        self.unstructured = unstructured
        self.type = type
        if source is not None:
            self.source = source
        if object is not None:
            self.object = object
        if when is not None:
            self.when = when
        if action_id is not None:
            self.action_id = action_id
        if relevant_state is not None:
            self.relevant_state = relevant_state

    @property
    def unstructured(self):
        """Gets the unstructured of this Event.  # noqa: E501

        Natural language, plain text description of the event  # noqa: E501

        :return: The unstructured of this Event.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Event.

        Natural language, plain text description of the event  # noqa: E501

        :param unstructured: The unstructured of this Event.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def type(self):
        """Gets the type of this Event.  # noqa: E501


        :return: The type of this Event.  # noqa: E501
        :rtype: EventTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Event.


        :param type: The type of this Event.  # noqa: E501
        :type: EventTypeEnum
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def source(self):
        """Gets the source of this Event.  # noqa: E501

        The 'subject' of the event; can be a character `id` or an `EntityTypeEnum`  # noqa: E501

        :return: The source of this Event.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Event.

        The 'subject' of the event; can be a character `id` or an `EntityTypeEnum`  # noqa: E501

        :param source: The source of this Event.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def object(self):
        """Gets the object of this Event.  # noqa: E501

        The 'object' of the event; can be a character `id` or an `EntityTypeEnum`  # noqa: E501

        :return: The object of this Event.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Event.

        The 'object' of the event; can be a character `id` or an `EntityTypeEnum`  # noqa: E501

        :param object: The object of this Event.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def when(self):
        """Gets the when of this Event.  # noqa: E501

        indicates when (in minutes) the event happened (negative value) or is expected to happen (positive value); omit if zero (event happens now)  # noqa: E501

        :return: The when of this Event.  # noqa: E501
        :rtype: float
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this Event.

        indicates when (in minutes) the event happened (negative value) or is expected to happen (positive value); omit if zero (event happens now)  # noqa: E501

        :param when: The when of this Event.  # noqa: E501
        :type: float
        """

        self._when = when

    @property
    def action_id(self):
        """Gets the action_id of this Event.  # noqa: E501

        An action ID from among the available actions  # noqa: E501

        :return: The action_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this Event.

        An action ID from among the available actions  # noqa: E501

        :param action_id: The action_id of this Event.  # noqa: E501
        :type: str
        """

        self._action_id = action_id

    @property
    def relevant_state(self):
        """Gets the relevant_state of this Event.  # noqa: E501

        An array of relevant state for the Event  # noqa: E501

        :return: The relevant_state of this Event.  # noqa: E501
        :rtype: list[str]
        """
        return self._relevant_state

    @relevant_state.setter
    def relevant_state(self, relevant_state):
        """Sets the relevant_state of this Event.

        An array of relevant state for the Event  # noqa: E501

        :param relevant_state: The relevant_state of this Event.  # noqa: E501
        :type: list[str]
        """

        self._relevant_state = relevant_state

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
