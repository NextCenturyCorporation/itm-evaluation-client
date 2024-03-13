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

class MilitaryRankTitleEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PRIVATE_RECRUIT_ = "Private (Recruit)"
    PRIVATE = "Private"
    PRIVATE_FIRST_CLASS = "Private First Class"
    SPECIALIST = "Specialist"
    CORPORAL = "Corporal"
    SERGEANT = "Sergeant"
    STAFF_SERGEANT = "Staff Sergeant"
    SERGEANT_FIRST_CLASS = "Sergeant First Class"
    MASTER_SERGEANT = "Master Sergeant"
    FIRST_SERGEANT = "First Sergeant"
    SERGEANT_MAJOR = "Sergeant Major"
    COMMAND_SERGEANT_MAJOR = "Command Sergeant Major"
    SERGEANT_MAJOR_OF_THE_ARMY = "Sergeant Major of the Army"
    WARRANT_OFFICER_1 = "Warrant Officer 1"
    CHIEF_WARRANT_OFFICER_2 = "Chief Warrant Officer 2"
    CHIEF_WARRANT_OFFICER_3 = "Chief Warrant Officer 3"
    CHIEF_WARRANT_OFFICER_4 = "Chief Warrant Officer 4"
    CHIEF_WARRANT_OFFICER_5 = "Chief Warrant Officer 5"
    _2ND_LIEUTENANT = "2nd Lieutenant"
    _1ST_LIEUTENANT = "1st Lieutenant"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    MAJOR = "Major"
    LIEUTENANT_COLONEL = "Lieutenant Colonel"
    COLONEL = "Colonel"
    BRIGADIER_GENERAL = "Brigadier General"
    MAJOR_GENERAL = "Major General"
    LIEUTENANT_GENERAL = "Lieutenant General"
    ARMY_CHIEF_OF_STAFF_SPECIAL_ = "Army Chief of Staff (special)"
    GENERAL = "General"
    AIRMAN_BASIC = "Airman Basic"
    AIRMAN = "Airman"
    AIRMAN_FIRST_CLASS = "Airman First Class"
    SENIOR_AIRMAN = "Senior Airman"
    TECHNICAL_SERGEANT = "Technical Sergeant"
    SENIOR_MASTER_SERGEANT = "Senior Master Sergeant"
    FIRST_SERGEANT_CHIEF_MASTER_SERGEANT = "First Sergeant / Chief Master Sergeant"
    CHIEF_MASTER_SERGEANT_OF_THE_AIR_FORCE = "Chief Master Sergeant of the Air Force"
    AIR_FORCE_CHIEF_OF_STAFF_SPECIAL_ = "Air Force Chief of Staff (special)"
    SEAMAN_RECRUIT = "Seaman Recruit"
    SEAMAN_APPRENTICE = "Seaman Apprentice"
    SEAMAN = "Seaman"
    PETTY_OFFICER_THIRD_CLASS = "Petty Officer Third Class"
    PETTY_OFFICER_SECOND_CLASS = "Petty Officer Second Class"
    PETTY_OFFICER_FIRST_CLASS = "Petty Officer First Class"
    CHIEF_PETTY_OFFICER = "Chief Petty Officer"
    SENIOR_CHIEF_PETTY_OFFICER = "Senior Chief Petty Officer"
    MASTER_CHIEF_PETTY_OFFICER = "Master Chief Petty Officer"
    MASTER_CHIEF_PETTY_OFFICER_OF_THE_NAVY = "Master Chief Petty Officer of the Navy"
    MASTER_CHIEF_PETTY_OFFICER_OF_THE_COAST_GUARD = "Master Chief Petty Officer of the Coast Guard"
    CHIEF_WARRANT_OFFICER = "Chief Warrant Officer"
    ENSIGN = "Ensign"
    LIEUTENANT_JUNIOR_GRADE = "Lieutenant, Junior Grade"
    LIEUTENANT_COMMANDER = "Lieutenant Commander"
    COMMANDER = "Commander"
    REAR_ADMIRAL_LOWER_HALF_ = "Rear Admiral (Lower Half)"
    REAR_ADMIRAL_UPPER_HALF_ = "Rear Admiral (Upper Half)"
    VICE_ADMIRAL = "Vice Admiral"
    CHIEF_OF_NAVAL_OPERATIONS_SPECIAL_ = "Chief of Naval Operations (special)"
    COMMANDANT_OF_THE_COAST_GUARD_SPECIAL_ = "Commandant of the Coast Guard (special)"
    ADMIRAL = "Admiral"
    LANCE_CORPORAL = "Lance Corporal"
    GUNNERY_SERGEANT = "Gunnery Sergeant"
    MASTER_GUNNERY_SERGEANT = "Master Gunnery Sergeant"
    SERGEANT_MAJOR_OF_THE_MARINE_CORPS = "Sergeant Major of the Marine Corps"
    WARRANT_OFFICER = "Warrant Officer"
    COMMANDANT_OF_THE_MARINE_CORPS = "Commandant of the Marine Corps"
    SPECIALIST_1 = "Specialist 1"
    SPECIALIST_2 = "Specialist 2"
    SPECIALIST_3 = "Specialist 3"
    SPECIALIST_4 = "Specialist 4"
    CHIEF_MASTER_SERGEANT = "Chief Master Sergeant"
    CHIEF_MASTER_SERGEANT_OF_THE_SPACE_FORCE = "Chief Master Sergeant of the Space Force"
    CHIEF_OF_SPACE_OPERATIONS = "Chief of Space Operations"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """MilitaryRankTitleEnum - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(MilitaryRankTitleEnum, dict):
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
        if not isinstance(other, MilitaryRankTitleEnum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
