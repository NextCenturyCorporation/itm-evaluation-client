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

class AlignmentResults(object):
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
        'alignment_source': 'list[AlignmentSource]',
        'alignment_target_id': 'str',
        'score': 'float'
    }

    attribute_map = {
        'alignment_source': 'alignment_source',
        'alignment_target_id': 'alignment_target_id',
        'score': 'score'
    }

    def __init__(self, alignment_source=None, alignment_target_id=None, score=None):  # noqa: E501
        """AlignmentResults - a model defined in Swagger"""  # noqa: E501
        self._alignment_source = None
        self._alignment_target_id = None
        self._score = None
        self.discriminator = None
        self.alignment_source = alignment_source
        self.alignment_target_id = alignment_target_id
        self.score = score

    @property
    def alignment_source(self):
        """Gets the alignment_source of this AlignmentResults.  # noqa: E501


        :return: The alignment_source of this AlignmentResults.  # noqa: E501
        :rtype: list[AlignmentSource]
        """
        return self._alignment_source

    @alignment_source.setter
    def alignment_source(self, alignment_source):
        """Sets the alignment_source of this AlignmentResults.


        :param alignment_source: The alignment_source of this AlignmentResults.  # noqa: E501
        :type: list[AlignmentSource]
        """
        if alignment_source is None:
            raise ValueError("Invalid value for `alignment_source`, must not be `None`")  # noqa: E501

        self._alignment_source = alignment_source

    @property
    def alignment_target_id(self):
        """Gets the alignment_target_id of this AlignmentResults.  # noqa: E501

        ID of desired profile to align responses to.  # noqa: E501

        :return: The alignment_target_id of this AlignmentResults.  # noqa: E501
        :rtype: str
        """
        return self._alignment_target_id

    @alignment_target_id.setter
    def alignment_target_id(self, alignment_target_id):
        """Sets the alignment_target_id of this AlignmentResults.

        ID of desired profile to align responses to.  # noqa: E501

        :param alignment_target_id: The alignment_target_id of this AlignmentResults.  # noqa: E501
        :type: str
        """
        if alignment_target_id is None:
            raise ValueError("Invalid value for `alignment_target_id`, must not be `None`")  # noqa: E501

        self._alignment_target_id = alignment_target_id

    @property
    def score(self):
        """Gets the score of this AlignmentResults.  # noqa: E501

        Measured alignment, 0 (completely unaligned) - 1 (completely aligned).  # noqa: E501

        :return: The score of this AlignmentResults.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this AlignmentResults.

        Measured alignment, 0 (completely unaligned) - 1 (completely aligned).  # noqa: E501

        :param score: The score of this AlignmentResults.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

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
        if issubclass(AlignmentResults, dict):
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
        if not isinstance(other, AlignmentResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
