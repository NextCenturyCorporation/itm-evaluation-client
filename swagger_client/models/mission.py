# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Dry Run Evaluation.  The API is based on the OpenAPI 3.0.3 specification.  # noqa: E501

    OpenAPI spec version: 0.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Mission(object):
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
        'mission_type': 'MissionTypeEnum',
        'character_importance': 'list[dict(str, MissionImportanceEnum)]',
        'civilian_presence': 'CivilianPresenceEnum',
        'communication_capability': 'CommunicationCapabilityEnum',
        'roe': 'str',
        'political_climate': 'str',
        'medical_policies': 'list[MedicalPoliciesEnum]'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'mission_type': 'mission_type',
        'character_importance': 'character_importance',
        'civilian_presence': 'civilian_presence',
        'communication_capability': 'communication_capability',
        'roe': 'roe',
        'political_climate': 'political_climate',
        'medical_policies': 'medical_policies'
    }

    def __init__(self, unstructured=None, mission_type=None, character_importance=None, civilian_presence=None, communication_capability=None, roe=None, political_climate=None, medical_policies=None):  # noqa: E501
        """Mission - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._mission_type = None
        self._character_importance = None
        self._civilian_presence = None
        self._communication_capability = None
        self._roe = None
        self._political_climate = None
        self._medical_policies = None
        self.discriminator = None
        self.unstructured = unstructured
        self.mission_type = mission_type
        if character_importance is not None:
            self.character_importance = character_importance
        if civilian_presence is not None:
            self.civilian_presence = civilian_presence
        if communication_capability is not None:
            self.communication_capability = communication_capability
        if roe is not None:
            self.roe = roe
        if political_climate is not None:
            self.political_climate = political_climate
        if medical_policies is not None:
            self.medical_policies = medical_policies

    @property
    def unstructured(self):
        """Gets the unstructured of this Mission.  # noqa: E501

        natural language description of current mission  # noqa: E501

        :return: The unstructured of this Mission.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this Mission.

        natural language description of current mission  # noqa: E501

        :param unstructured: The unstructured of this Mission.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def mission_type(self):
        """Gets the mission_type of this Mission.  # noqa: E501


        :return: The mission_type of this Mission.  # noqa: E501
        :rtype: MissionTypeEnum
        """
        return self._mission_type

    @mission_type.setter
    def mission_type(self, mission_type):
        """Sets the mission_type of this Mission.


        :param mission_type: The mission_type of this Mission.  # noqa: E501
        :type: MissionTypeEnum
        """
        if mission_type is None:
            raise ValueError("Invalid value for `mission_type`, must not be `None`")  # noqa: E501

        self._mission_type = mission_type

    @property
    def character_importance(self):
        """Gets the character_importance of this Mission.  # noqa: E501

        A list of pairs of character ids with an indicator of how mission-critical the character is  # noqa: E501

        :return: The character_importance of this Mission.  # noqa: E501
        :rtype: list[dict(str, MissionImportanceEnum)]
        """
        return self._character_importance

    @character_importance.setter
    def character_importance(self, character_importance):
        """Sets the character_importance of this Mission.

        A list of pairs of character ids with an indicator of how mission-critical the character is  # noqa: E501

        :param character_importance: The character_importance of this Mission.  # noqa: E501
        :type: list[dict(str, MissionImportanceEnum)]
        """

        self._character_importance = character_importance

    @property
    def civilian_presence(self):
        """Gets the civilian_presence of this Mission.  # noqa: E501


        :return: The civilian_presence of this Mission.  # noqa: E501
        :rtype: CivilianPresenceEnum
        """
        return self._civilian_presence

    @civilian_presence.setter
    def civilian_presence(self, civilian_presence):
        """Sets the civilian_presence of this Mission.


        :param civilian_presence: The civilian_presence of this Mission.  # noqa: E501
        :type: CivilianPresenceEnum
        """

        self._civilian_presence = civilian_presence

    @property
    def communication_capability(self):
        """Gets the communication_capability of this Mission.  # noqa: E501


        :return: The communication_capability of this Mission.  # noqa: E501
        :rtype: CommunicationCapabilityEnum
        """
        return self._communication_capability

    @communication_capability.setter
    def communication_capability(self, communication_capability):
        """Sets the communication_capability of this Mission.


        :param communication_capability: The communication_capability of this Mission.  # noqa: E501
        :type: CommunicationCapabilityEnum
        """

        self._communication_capability = communication_capability

    @property
    def roe(self):
        """Gets the roe of this Mission.  # noqa: E501

        rules of engagement to inform decision-making, but not to restrict decision space  # noqa: E501

        :return: The roe of this Mission.  # noqa: E501
        :rtype: str
        """
        return self._roe

    @roe.setter
    def roe(self, roe):
        """Sets the roe of this Mission.

        rules of engagement to inform decision-making, but not to restrict decision space  # noqa: E501

        :param roe: The roe of this Mission.  # noqa: E501
        :type: str
        """

        self._roe = roe

    @property
    def political_climate(self):
        """Gets the political_climate of this Mission.  # noqa: E501

        The political climate in a mission to inform decision-making  # noqa: E501

        :return: The political_climate of this Mission.  # noqa: E501
        :rtype: str
        """
        return self._political_climate

    @political_climate.setter
    def political_climate(self, political_climate):
        """Sets the political_climate of this Mission.

        The political climate in a mission to inform decision-making  # noqa: E501

        :param political_climate: The political_climate of this Mission.  # noqa: E501
        :type: str
        """

        self._political_climate = political_climate

    @property
    def medical_policies(self):
        """Gets the medical_policies of this Mission.  # noqa: E501

        A list of medical policies; omit this property if no special policy is in place  # noqa: E501

        :return: The medical_policies of this Mission.  # noqa: E501
        :rtype: list[MedicalPoliciesEnum]
        """
        return self._medical_policies

    @medical_policies.setter
    def medical_policies(self, medical_policies):
        """Sets the medical_policies of this Mission.

        A list of medical policies; omit this property if no special policy is in place  # noqa: E501

        :param medical_policies: The medical_policies of this Mission.  # noqa: E501
        :type: list[MedicalPoliciesEnum]
        """

        self._medical_policies = medical_policies

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
        if issubclass(Mission, dict):
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
        if not isinstance(other, Mission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
