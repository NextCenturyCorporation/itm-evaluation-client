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

class Action(object):
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
        'action_id': 'str',
        'action_type': 'ActionTypeEnum',
        'intent_action': 'bool',
        'unstructured': 'str',
        'character_id': 'str',
        'threat_state': 'ThreatState',
        'parameters': 'dict(str, str)',
        'justification': 'str',
        'kdma_association': 'dict(str, float)'
    }

    attribute_map = {
        'action_id': 'action_id',
        'action_type': 'action_type',
        'intent_action': 'intent_action',
        'unstructured': 'unstructured',
        'character_id': 'character_id',
        'threat_state': 'threat_state',
        'parameters': 'parameters',
        'justification': 'justification',
        'kdma_association': 'kdma_association'
    }

    def __init__(self, action_id=None, action_type=None, intent_action=False, unstructured=None, character_id=None, threat_state=None, parameters=None, justification=None, kdma_association=None):  # noqa: E501
        """Action - a model defined in Swagger"""  # noqa: E501
        self._action_id = None
        self._action_type = None
        self._intent_action = None
        self._unstructured = None
        self._character_id = None
        self._threat_state = None
        self._parameters = None
        self._justification = None
        self._kdma_association = None
        self.discriminator = None
        self.action_id = action_id
        self.action_type = action_type
        if intent_action is not None:
            self.intent_action = intent_action
        if unstructured is not None:
            self.unstructured = unstructured
        if character_id is not None:
            self.character_id = character_id
        if threat_state is not None:
            self.threat_state = threat_state
        if parameters is not None:
            self.parameters = parameters
        if justification is not None:
            self.justification = justification
        if kdma_association is not None:
            self.kdma_association = kdma_association

    @property
    def action_id(self):
        """Gets the action_id of this Action.  # noqa: E501

        A unique action ID within the scenario  # noqa: E501

        :return: The action_id of this Action.  # noqa: E501
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this Action.

        A unique action ID within the scenario  # noqa: E501

        :param action_id: The action_id of this Action.  # noqa: E501
        :type: str
        """
        if action_id is None:
            raise ValueError("Invalid value for `action_id`, must not be `None`")  # noqa: E501

        self._action_id = action_id

    @property
    def action_type(self):
        """Gets the action_type of this Action.  # noqa: E501


        :return: The action_type of this Action.  # noqa: E501
        :rtype: ActionTypeEnum
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this Action.


        :param action_type: The action_type of this Action.  # noqa: E501
        :type: ActionTypeEnum
        """
        if action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501

        self._action_type = action_type

    @property
    def intent_action(self):
        """Gets the intent_action of this Action.  # noqa: E501

        Whether this action is to be taken or intended  # noqa: E501

        :return: The intent_action of this Action.  # noqa: E501
        :rtype: bool
        """
        return self._intent_action

    @intent_action.setter
    def intent_action(self, intent_action):
        """Sets the intent_action of this Action.

        Whether this action is to be taken or intended  # noqa: E501

        :param intent_action: The intent_action of this Action.  # noqa: E501
        :type: bool
        """

        self._intent_action = intent_action

    @property
    def unstructured(self):
        """Gets the unstructured of this Action.  # noqa: E501

        Natural language, plain text description of the action  # noqa: E501

        :return: The unstructured of this Action.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Action.

        Natural language, plain text description of the action  # noqa: E501

        :param unstructured: The unstructured of this Action.  # noqa: E501
        :type: str
        """

        self._unstructured = unstructured

    @property
    def character_id(self):
        """Gets the character_id of this Action.  # noqa: E501

        The ID of the character being acted upon  # noqa: E501

        :return: The character_id of this Action.  # noqa: E501
        :rtype: str
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this Action.

        The ID of the character being acted upon  # noqa: E501

        :param character_id: The character_id of this Action.  # noqa: E501
        :type: str
        """

        self._character_id = character_id

    @property
    def threat_state(self):
        """Gets the threat_state of this Action.  # noqa: E501


        :return: The threat_state of this Action.  # noqa: E501
        :rtype: ThreatState
        """
        return self._threat_state

    @threat_state.setter
    def threat_state(self, threat_state):
        """Sets the threat_state of this Action.


        :param threat_state: The threat_state of this Action.  # noqa: E501
        :type: ThreatState
        """

        self._threat_state = threat_state

    @property
    def parameters(self):
        """Gets the parameters of this Action.  # noqa: E501

        key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab=readme-ov-file#available-actions)  # noqa: E501

        :return: The parameters of this Action.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Action.

        key-value pairs containing additional [action-specific parameters](https://github.com/NextCenturyCorporation/itm-evaluation-client?tab=readme-ov-file#available-actions)  # noqa: E501

        :param parameters: The parameters of this Action.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def justification(self):
        """Gets the justification of this Action.  # noqa: E501

        A justification of the action taken  # noqa: E501

        :return: The justification of this Action.  # noqa: E501
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """Sets the justification of this Action.

        A justification of the action taken  # noqa: E501

        :param justification: The justification of this Action.  # noqa: E501
        :type: str
        """

        self._justification = justification

    @property
    def kdma_association(self):
        """Gets the kdma_association of this Action.  # noqa: E501

        KDMA associations for this choice, if provided by TA1  # noqa: E501

        :return: The kdma_association of this Action.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._kdma_association

    @kdma_association.setter
    def kdma_association(self, kdma_association):
        """Sets the kdma_association of this Action.

        KDMA associations for this choice, if provided by TA1  # noqa: E501

        :param kdma_association: The kdma_association of this Action.  # noqa: E501
        :type: dict(str, float)
        """

        self._kdma_association = kdma_association

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
        if issubclass(Action, dict):
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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other