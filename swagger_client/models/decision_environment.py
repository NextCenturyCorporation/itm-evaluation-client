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

class DecisionEnvironment(object):
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
        'aid': 'list[Aid]',
        'movement_restriction': 'MovementRestrictionEnum',
        'sound_restriction': 'SoundRestrictionEnum',
        'oxygen_levels': 'OxygenLevelsEnum',
        'population_density': 'PopulationDensityEnum',
        'injury_triggers': 'InjuryTriggerEnum',
        'air_quality': 'AirQualityEnum',
        'city_infrastructure': 'str'
    }

    attribute_map = {
        'unstructured': 'unstructured',
        'aid': 'aid',
        'movement_restriction': 'movement_restriction',
        'sound_restriction': 'sound_restriction',
        'oxygen_levels': 'oxygen_levels',
        'population_density': 'population_density',
        'injury_triggers': 'injury_triggers',
        'air_quality': 'air_quality',
        'city_infrastructure': 'city_infrastructure'
    }

    def __init__(self, unstructured=None, aid=None, movement_restriction=None, sound_restriction=None, oxygen_levels=None, population_density=None, injury_triggers=None, air_quality=None, city_infrastructure=None):  # noqa: E501
        """DecisionEnvironment - a model defined in Swagger"""  # noqa: E501
        self._unstructured = None
        self._aid = None
        self._movement_restriction = None
        self._sound_restriction = None
        self._oxygen_levels = None
        self._population_density = None
        self._injury_triggers = None
        self._air_quality = None
        self._city_infrastructure = None
        self.discriminator = None
        self.unstructured = unstructured
        if aid is not None:
            self.aid = aid
        if movement_restriction is not None:
            self.movement_restriction = movement_restriction
        if sound_restriction is not None:
            self.sound_restriction = sound_restriction
        if oxygen_levels is not None:
            self.oxygen_levels = oxygen_levels
        if population_density is not None:
            self.population_density = population_density
        if injury_triggers is not None:
            self.injury_triggers = injury_triggers
        if air_quality is not None:
            self.air_quality = air_quality
        if city_infrastructure is not None:
            self.city_infrastructure = city_infrastructure

    @property
    def unstructured(self):
        """Gets the unstructured of this DecisionEnvironment.  # noqa: E501

        Natural language, plain text description of decision-impacting environmental factors  # noqa: E501

        :return: The unstructured of this DecisionEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._unstructured

    @unstructured.setter
    def unstructured(self, unstructured):
        """Sets the unstructured of this DecisionEnvironment.

        Natural language, plain text description of decision-impacting environmental factors  # noqa: E501

        :param unstructured: The unstructured of this DecisionEnvironment.  # noqa: E501
        :type: str
        """
        if unstructured is None:
            raise ValueError("Invalid value for `unstructured`, must not be `None`")  # noqa: E501

        self._unstructured = unstructured

    @property
    def aid(self):
        """Gets the aid of this DecisionEnvironment.  # noqa: E501

        A list of available forms of aid  # noqa: E501

        :return: The aid of this DecisionEnvironment.  # noqa: E501
        :rtype: list[Aid]
        """
        return self._aid

    @aid.setter
    def aid(self, aid):
        """Sets the aid of this DecisionEnvironment.

        A list of available forms of aid  # noqa: E501

        :param aid: The aid of this DecisionEnvironment.  # noqa: E501
        :type: list[Aid]
        """

        self._aid = aid

    @property
    def movement_restriction(self):
        """Gets the movement_restriction of this DecisionEnvironment.  # noqa: E501


        :return: The movement_restriction of this DecisionEnvironment.  # noqa: E501
        :rtype: MovementRestrictionEnum
        """
        return self._movement_restriction

    @movement_restriction.setter
    def movement_restriction(self, movement_restriction):
        """Sets the movement_restriction of this DecisionEnvironment.


        :param movement_restriction: The movement_restriction of this DecisionEnvironment.  # noqa: E501
        :type: MovementRestrictionEnum
        """

        self._movement_restriction = movement_restriction

    @property
    def sound_restriction(self):
        """Gets the sound_restriction of this DecisionEnvironment.  # noqa: E501


        :return: The sound_restriction of this DecisionEnvironment.  # noqa: E501
        :rtype: SoundRestrictionEnum
        """
        return self._sound_restriction

    @sound_restriction.setter
    def sound_restriction(self, sound_restriction):
        """Sets the sound_restriction of this DecisionEnvironment.


        :param sound_restriction: The sound_restriction of this DecisionEnvironment.  # noqa: E501
        :type: SoundRestrictionEnum
        """

        self._sound_restriction = sound_restriction

    @property
    def oxygen_levels(self):
        """Gets the oxygen_levels of this DecisionEnvironment.  # noqa: E501


        :return: The oxygen_levels of this DecisionEnvironment.  # noqa: E501
        :rtype: OxygenLevelsEnum
        """
        return self._oxygen_levels

    @oxygen_levels.setter
    def oxygen_levels(self, oxygen_levels):
        """Sets the oxygen_levels of this DecisionEnvironment.


        :param oxygen_levels: The oxygen_levels of this DecisionEnvironment.  # noqa: E501
        :type: OxygenLevelsEnum
        """

        self._oxygen_levels = oxygen_levels

    @property
    def population_density(self):
        """Gets the population_density of this DecisionEnvironment.  # noqa: E501


        :return: The population_density of this DecisionEnvironment.  # noqa: E501
        :rtype: PopulationDensityEnum
        """
        return self._population_density

    @population_density.setter
    def population_density(self, population_density):
        """Sets the population_density of this DecisionEnvironment.


        :param population_density: The population_density of this DecisionEnvironment.  # noqa: E501
        :type: PopulationDensityEnum
        """

        self._population_density = population_density

    @property
    def injury_triggers(self):
        """Gets the injury_triggers of this DecisionEnvironment.  # noqa: E501


        :return: The injury_triggers of this DecisionEnvironment.  # noqa: E501
        :rtype: InjuryTriggerEnum
        """
        return self._injury_triggers

    @injury_triggers.setter
    def injury_triggers(self, injury_triggers):
        """Sets the injury_triggers of this DecisionEnvironment.


        :param injury_triggers: The injury_triggers of this DecisionEnvironment.  # noqa: E501
        :type: InjuryTriggerEnum
        """

        self._injury_triggers = injury_triggers

    @property
    def air_quality(self):
        """Gets the air_quality of this DecisionEnvironment.  # noqa: E501


        :return: The air_quality of this DecisionEnvironment.  # noqa: E501
        :rtype: AirQualityEnum
        """
        return self._air_quality

    @air_quality.setter
    def air_quality(self, air_quality):
        """Sets the air_quality of this DecisionEnvironment.


        :param air_quality: The air_quality of this DecisionEnvironment.  # noqa: E501
        :type: AirQualityEnum
        """

        self._air_quality = air_quality

    @property
    def city_infrastructure(self):
        """Gets the city_infrastructure of this DecisionEnvironment.  # noqa: E501

        Refers to building/city infrastructure that should be noted and known (safe house, etc.)  # noqa: E501

        :return: The city_infrastructure of this DecisionEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._city_infrastructure

    @city_infrastructure.setter
    def city_infrastructure(self, city_infrastructure):
        """Sets the city_infrastructure of this DecisionEnvironment.

        Refers to building/city infrastructure that should be noted and known (safe house, etc.)  # noqa: E501

        :param city_infrastructure: The city_infrastructure of this DecisionEnvironment.  # noqa: E501
        :type: str
        """

        self._city_infrastructure = city_infrastructure

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
        if issubclass(DecisionEnvironment, dict):
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
        if not isinstance(other, DecisionEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
